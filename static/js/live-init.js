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

  const statusContainer = document.getElementById("exercise-loading-status");
  const indicatorContainer = document.getElementById("exercise-loading-indicator");
  if (!indicatorContainer) return;

  const needsPyodide = document.querySelector('script[type="pyodide-data"]');
  const needsWebR = document.querySelector('script[type="webr-data"]');
  if (!needsPyodide && !needsWebR) return;

  indicatorContainer.classList.remove("d-none");

  function createStatusText(label) {
    const el = document.createElement("div");
    el.classList = "exercise-loading-details";
    el.textContent = label;
    statusContainer.appendChild(el);
    return el;
  }

  function hideLoadingWhenDone(statusText) {
    statusText.remove();
    if (statusContainer.children.length === 0) indicatorContainer.remove();
  }

  function showError(statusText, err) {
    statusText.style.color = "var(--exercise-editor-hl-er, #AD0000)";
    statusText.textContent = err.message;
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
    const statusText = createStatusText("Initialise");

    pyodidePromise = (async () => {
      statusText.textContent = "Downloading Pyodide";
      const pyodide = await startPyodideWorker(data.options);

      statusText.textContent = "Downloading package: micropip";
      await pyodide.loadPackage("micropip");
      const micropip = await pyodide.pyimport("micropip");
      for (const pkg of data.packages.pkgs) {
        statusText.textContent = `Downloading package: ${pkg}`;
        await micropip.install(pkg);
      }
      await micropip.destroy();

      await mountFiles(pyodide.FS, files, async (path) => {
        try { await pyodide.FS.mkdir(path); } catch (e) {
          if (e.name !== "ErrnoError") throw e;
        }
      });

      statusText.textContent = "Pyodide environment setup";
      await setupPython(pyodide);
      hideLoadingWhenDone(statusText);
      return pyodide;
    })().catch((err) => { showError(statusText, err); throw err; });
  }

  // Initialize webR
  let webRPromise = null;
  if (needsWebR) {
    const data = JSON.parse(b64Decode(needsWebR.textContent));
    const filesEl = document.querySelector('script[type="vfs-file"]');
    const files = filesEl ? JSON.parse(b64Decode(filesEl.textContent)) : [];
    const { WebR } = runtime.WebR;
    const statusText = createStatusText("Initialise");

    webRPromise = (async () => {
      statusText.textContent = "Downloading webR";
      const webR = new WebR(data.options);
      await webR.init();

      data.packages.repos.push("https://repo.r-wasm.org");
      for (const pkg of data.packages.pkgs) {
        statusText.textContent = `Downloading package: ${pkg}`;
        await webR.evalRVoid(
          `webr::install(pkg, repos = repos)\nlibrary(pkg, character.only = TRUE)`,
          { env: { pkg, repos: data.packages.repos } }
        );
      }

      await mountFiles(webR.FS, files, async (path) => {
        const analysis = await webR.FS.analyzePath(path);
        if (!analysis.exists) await webR.FS.mkdir(path);
      });

      statusText.textContent = "Installing webR shims";
      await webR.evalRVoid("webr::shim_install()");
      statusText.textContent = "WebR environment setup";
      await setupR(webR, data);
      hideLoadingWhenDone(statusText);
      return webR;
    })().catch((err) => { showError(statusText, err); throw err; });
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
    cell.appendChild(outputContainer);

    editor.container.addEventListener("input", async (e) => {
      if (!e.detail || !e.detail.commit) return;
      const result = await process(editor.container.value, {});
      outputContainer.replaceChildren(result);

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
})();
