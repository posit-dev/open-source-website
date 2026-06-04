(async function () {
  const runtime = window._exercise_ojs_runtime;
  if (!runtime) return;

  document.documentElement.classList.add("quarto-light");

  // Pyodide runs in a Web Worker via Comlink. Values that should be primitives
  // (strings, null) arrive as proxy objects. We patch evaluate() to materialize
  // all output data before asHtml() tries to use it in template literals.
  const OrigEvaluate = runtime.PyodideEvaluator.prototype.evaluate;
  runtime.PyodideEvaluator.prototype.evaluate = async function (...args) {
    const result = await OrigEvaluate.apply(this, args);
    if (!result) return result;

    if (result.stdout != null && typeof result.stdout !== "string") {
      try { result.stdout = String(await result.stdout.valueOf()); } catch { result.stdout = ""; }
    }
    if (result.stderr != null && typeof result.stderr !== "string") {
      try { result.stderr = String(await result.stderr.valueOf()); } catch { result.stderr = ""; }
    }

    if (result.outputs != null && typeof result.outputs.length !== "number") {
      const mimeTypes = [
        "application/html-imagebitmap", "text/html",
        "application/vnd.jupyter.widget-view+json",
        "application/vnd.plotly.v1+json", "text/plain",
        "image/png", "image/jpeg", "image/gif", "image/svg+xml",
      ];
      const len = await result.outputs.length;
      const resolved = [];
      for (let i = 0; i < len; i++) {
        const item = await result.outputs.get(i);
        const mimeData = {};
        for (const mime of mimeTypes) {
          try {
            const val = await item._repr_mime_(mime);
            if (val == null) {
              mimeData[mime] = null;
            } else if (typeof val === "string" || val instanceof ImageBitmap) {
              mimeData[mime] = val;
            } else {
              try { mimeData[mime] = "" + (await val.valueOf()); } catch { mimeData[mime] = null; }
            }
          } catch {
            mimeData[mime] = null;
          }
        }
        resolved.push({
          _repr_mime_(mime) { return mimeData[mime]; },
          destroy() { try { item.destroy(); } catch {} },
        });
      }
      result.outputs = { length: len, get(i) { return resolved[i]; } };
    }

    return result;
  };

  const {
    PyodideExerciseEditor, PyodideEvaluator, PyodideGrader,
    WebRExerciseEditor, WebREvaluator, WebRGrader,
    setupPython, setupR, startPyodideWorker,
    highlightPython, highlightR, b64Decode, collapsePath,
  } = runtime;

  const needsPyodide = document.querySelector('script[type="pyodide-data"]');
  const needsWebR = document.querySelector('script[type="webr-data"]');
  if (!needsPyodide && !needsWebR) return;

  // Track status indicators by engine type
  const statusByEngine = { pyodide: null, webr: null };

  function createStatusIndicator(engine, label) {
    // Create master status element
    const status = {
      label: label,
      elements: [] // Will hold DOM elements injected into each header
    };
    statusByEngine[engine] = status;
    return status;
  }

  function updateStatus(status, text) {
    status.label = text;
    status.elements.forEach(el => {
      const label = el.querySelector(".exercise-inline-loading-label");
      if (label) label.textContent = text;
    });
  }

  function hideStatus(status) {
    status.elements.forEach(el => el.remove());
    status.elements = [];
  }

  function showError(status, text) {
    status.label = text;
    status.elements.forEach(el => {
      // Hide the "Downloading:" prefix on error
      const prefix = el.querySelector(".exercise-inline-loading-prefix");
      if (prefix) prefix.style.display = "none";

      const label = el.querySelector(".exercise-inline-loading-label");
      if (label) {
        label.style.color = "var(--exercise-editor-hl-er, #AD0000)";
        label.textContent = text;
      }
      const spinner = el.querySelector(".spinner-grow");
      if (spinner) spinner.remove();
    });
  }

  function injectStatusIntoHeaders(engine) {
    const status = statusByEngine[engine];
    if (!status) return;

    // Find all headers for this engine type
    const headers = document.querySelectorAll(`.exercise-cell[data-engine="${engine}"] .card.exercise-editor .card-header`);

    headers.forEach(header => {
      // Find the right-side button container (it's the second child with d-flex)
      const buttonContainer = header.querySelector('.d-flex.align-items-center.gap-3:last-child');

      if (buttonContainer) {
        const el = document.createElement("div");
        el.className = "exercise-inline-loading-status";
        el.innerHTML = `<span class="exercise-inline-loading-prefix">Downloading:</span><span class="exercise-inline-loading-label">${status.label}</span><div class="spinner-grow spinner-grow-sm"></div>`;

        // Insert BEFORE the button group (first child of the button container)
        const firstChild = buttonContainer.firstChild;
        buttonContainer.insertBefore(el, firstChild);
        status.elements.push(el);
      }
    });
  }

  async function mountFiles(fs, files, mkdirFn) {
    for (const file of files) {
      const name = file.substring(file.lastIndexOf("/") + 1);
      const response = await fetch(file);
      if (!response.ok) {
        throw new Error(`Can't download \`${file}\`. Error ${response.status}: "${response.statusText}".`);
      }
      const data = await response.arrayBuffer();
      let filePath = file.includes("://") ? name : file;
      filePath = collapsePath(filePath);

      const parts = filePath.split("/").slice(0, -1);
      let path = "";
      while (parts.length > 0) {
        path += parts.shift() + "/";
        await mkdirFn(path);
      }
      await fs.writeFile(filePath, new Uint8Array(data));
    }
  }

  // Initialize Pyodide
  let pyodidePromise = null;
  if (needsPyodide) {
    const data = JSON.parse(b64Decode(needsPyodide.textContent));
    const filesEl = document.querySelector('script[type="vfs-file"]');
    const files = filesEl ? JSON.parse(b64Decode(filesEl.textContent)) : [];
    const status = createStatusIndicator("pyodide", "Initializing...");

    pyodidePromise = (async () => {
      updateStatus(status, "Pyodide");
      const pyodide = await startPyodideWorker(data.options);

      updateStatus(status, "micropip");
      await pyodide.loadPackage("micropip");
      const micropip = await pyodide.pyimport("micropip");
      for (const pkg of data.packages.pkgs) {
        updateStatus(status, pkg);
        await micropip.install(pkg);
      }
      await micropip.destroy();

      await mountFiles(pyodide.FS, files, async (path) => {
        try { await pyodide.FS.mkdir(path); } catch (e) {
          if (e.name !== "ErrnoError") throw e;
        }
      });

      updateStatus(status, "Python setup");
      await setupPython(pyodide);
      hideStatus(status);
      return pyodide;
    })().catch((err) => { showError(status, err.message); throw err; });
  }

  // Initialize webR
  let webRPromise = null;
  if (needsWebR) {
    const data = JSON.parse(b64Decode(needsWebR.textContent));
    const filesEl = document.querySelector('script[type="vfs-file"]');
    const files = filesEl ? JSON.parse(b64Decode(filesEl.textContent)) : [];
    const { WebR } = runtime.WebR;
    const status = createStatusIndicator("webr", "Initializing...");

    webRPromise = (async () => {
      updateStatus(status, "webR");
      const webR = new WebR(data.options);
      await webR.init();

      data.packages.repos.push("https://repo.r-wasm.org");
      for (const pkg of data.packages.pkgs) {
        updateStatus(status, pkg);
        await webR.evalRVoid(
          `webr::install(pkg, repos = repos)\nlibrary(pkg, character.only = TRUE)`,
          { env: { pkg, repos: data.packages.repos } }
        );
      }

      await mountFiles(webR.FS, files, async (path) => {
        const analysis = await webR.FS.analyzePath(path);
        if (!analysis.exists) await webR.FS.mkdir(path);
      });

      updateStatus(status, "R shims");
      await webR.evalRVoid("webr::shim_install()");
      updateStatus(status, "R setup");
      await setupR(webR, data);
      hideStatus(status);
      return webR;
    })().catch((err) => { showError(status, err.message); throw err; });
  }

  // Process helper matching the OJS evaluate pattern
  function makeProcess(runtimePromise, EvaluatorClass) {
    return async (context, inputs) => {
      const instance = await runtimePromise;
      const evaluator = new EvaluatorClass(instance, context);
      await evaluator.process(inputs);
      return evaluator.container;
    };
  }

  // Wire up an editable cell: listen for Run clicks, enable button when ready
  function wireEditor(editor, cell, runtimePromise, process, GraderClass) {
    const outputContainer = document.createElement("div");
    outputContainer.className = "exercise-output-container";
    cell.appendChild(outputContainer);

    let isCollapsing = false;
    let allowStartOver = false;

    // Watch for Start Over button clicks and animate collapse
    editor.container.addEventListener("click", (e) => {
      const target = e.target.closest('a[aria-label="Start Over"]');
      if (target) {
        // If we've already animated, let it through
        if (allowStartOver) {
          allowStartOver = false;
          return;
        }

        // Only animate if there's actual visible output (not just empty container)
        const hasOutput = outputContainer.children.length > 0 && outputContainer.offsetHeight > 0;
        if (hasOutput) {
          e.preventDefault();
          e.stopPropagation();

          isCollapsing = true;

          // Capture current height and start collapse animation
          const currentHeight = outputContainer.offsetHeight;
          outputContainer.style.height = currentHeight + "px";
          outputContainer.style.overflow = "hidden";

          requestAnimationFrame(() => {
            outputContainer.style.height = "0px";
          });

          // After animation, keep at 0 and trigger the actual Start Over
          setTimeout(() => {
            // Keep height at 0 and let Start Over clear naturally
            isCollapsing = false;

            // Now trigger the actual Start Over behavior
            allowStartOver = true;
            target.click();

            // Reset styles after Start Over has processed
            setTimeout(() => {
              outputContainer.style.height = "";
              outputContainer.style.overflow = "";
            }, 50);
          }, 310);

          return false;
        } else {
          // No output, but lock everything at 0 to prevent any layout shift
          const originalPadding = outputContainer.style.padding;
          const originalMargin = outputContainer.style.margin;

          outputContainer.style.height = "0px";
          outputContainer.style.minHeight = "0px";
          outputContainer.style.overflow = "hidden";
          outputContainer.style.padding = "0";
          outputContainer.style.margin = "0";

          // Reset after Start Over processes
          setTimeout(() => {
            outputContainer.style.height = "";
            outputContainer.style.minHeight = "";
            outputContainer.style.overflow = "";
            outputContainer.style.padding = originalPadding;
            outputContainer.style.margin = originalMargin;
          }, 50);
        }
      }
    }, true); // Use capture phase to intercept before editor handles it

    editor.container.addEventListener("input", async (e) => {
      if (!e.detail || !e.detail.commit) return;
      if (isCollapsing) return; // Skip if we're in the middle of collapsing

      // Show loading indicator - let it size naturally then transition
      const loader = document.createElement("div");
      loader.className = "exercise-output-loading";
      loader.innerHTML = `
        <div class="spinner-grow spinner-grow-sm"></div>
        <span>Running code...</span>
      `;

      // Measure loader height first
      loader.style.visibility = "hidden";
      outputContainer.replaceChildren(loader);
      const loaderHeight = loader.offsetHeight;
      loader.style.visibility = "";

      // Get starting height (might be 0 or might have previous output)
      const startHeight = outputContainer.offsetHeight || 0;
      outputContainer.style.height = startHeight + "px";
      outputContainer.style.overflow = "hidden";

      // Animate to loader height
      requestAnimationFrame(() => {
        outputContainer.style.height = loaderHeight + "px";
      });

      // Execute code
      const result = await process(editor.container.value, {});

      // Measure result height
      result.style.visibility = "hidden";
      outputContainer.appendChild(result);
      const resultHeight = result.offsetHeight;
      result.style.visibility = "";

      // Animate to result height
      outputContainer.replaceChildren(result);
      outputContainer.style.height = resultHeight + "px";

      // After transition, remove fixed height to allow natural sizing
      setTimeout(() => {
        outputContainer.style.height = "auto";
        outputContainer.style.overflow = "";
      }, 300);

      if (GraderClass && result.value && result.value.evaluator) {
        const grader = new GraderClass(result.value.evaluator);
        const feedback = await grader.gradeExercise();
        if (feedback) outputContainer.appendChild(feedback);
      }
    });

    runtimePromise.then(() => {
      editor.container.value.indicator.finished();
    });
  }

  // Process all exercise cells
  for (const cell of document.querySelectorAll(".exercise-cell")) {
    const id = cell.id;
    const engine = cell.dataset.engine;
    const scriptEl = document.querySelector(`script[type="${id}-contents"]`);
    if (!scriptEl) continue;

    const block = JSON.parse(b64Decode(scriptEl.textContent));
    const attr = block.attr;
    const code = block.code;

    const isPyodide = engine === "pyodide";
    const runtimePromise = isPyodide ? pyodidePromise : webRPromise;
    const EditorClass = isPyodide ? PyodideExerciseEditor : WebRExerciseEditor;
    const EvaluatorClass = isPyodide ? PyodideEvaluator : WebREvaluator;
    const GraderClass = isPyodide ? PyodideGrader : WebRGrader;
    const highlight = isPyodide ? highlightPython : highlightR;
    const process = makeProcess(runtimePromise, EvaluatorClass);

    if (attr.exercise && !attr.setup && !attr.check && !attr.hint && !attr.solution) {
      const options = Object.assign(
        { id: `${id}-contents`, envir: `exercise-env-${attr.exercise}`, error: false, caption: "Exercise" },
        attr
      );
      const editor = new EditorClass(runtimePromise, code, options);
      cell.appendChild(editor.container);
      wireEditor(editor, cell, runtimePromise, process, GraderClass);

    } else if (attr.edit === false || attr.edit === "false") {
      const options = Object.assign({ id: `${id}-contents`, echo: true, output: true }, attr);
      const container = document.createElement("div");

      if (options.echo !== false) {
        const preElem = document.createElement("pre");
        container.className = "sourceCode";
        preElem.className = `sourceCode ${isPyodide ? "python" : "r"}`;
        preElem.appendChild(highlight(code));
        preElem.style.position = "relative";
        const spinner = document.createElement("div");
        spinner.className = "spinner-grow spinner-grow-sm";
        spinner.style.cssText = "position:absolute;top:8px;right:8px";
        preElem.appendChild(spinner);
        container.appendChild(preElem);
      } else {
        const spinner = document.createElement("div");
        spinner.className = "spinner-grow spinner-grow-sm";
        container.appendChild(spinner);
      }

      cell.appendChild(container);
      (async () => {
        const result = await process({ code, options }, {});
        cell.replaceChild(result, container);
      })();

    } else {
      const options = Object.assign({ id: `${id}-contents` }, attr);
      const editor = new EditorClass(runtimePromise, code, options);
      cell.appendChild(editor.container);
      wireEditor(editor, cell, runtimePromise, process, null);
    }
  }

  // After editors are created, inject status indicators into their headers
  // Wait a tick for the DOM to settle
  setTimeout(() => {
    if (needsPyodide) injectStatusIntoHeaders("pyodide");
    if (needsWebR) injectStatusIntoHeaders("webr");
  }, 0);
})();
