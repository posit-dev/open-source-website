---
title: 'Neural networks in Orbital for Python 0.6.0: PyTorch straight to your database'
date: 2026-08-17T00:00:00.000Z
people:
  - Alessandro Molina
description: >
  Orbital 0.6.0 adds neural network support: PyTorch and scikit-learn MLPs
  compile to plain SQL, no Python runtime required at inference.
image: featured.png
image-alt: >-
  Diagram of a feed-forward neural network with input, hidden, and output layers
  flowing through the Python logo into a SQL-style data table, then into a
  database
topics:
  - Machine Learning
  - Artificial Intelligence
  - MLOps and Admin
software:
  - orbital-python
languages:
  - Python
  - SQL
tags:
  - Orbital
  - PyTorch
  - Neural Networks
  - Python Packages
hidesubscription: false
---


Over the past couple of months I've been teaching Orbital to speak PyTorch.

Orbital's whole pitch is that a trained model becomes SQL, so a database can run predictions on its own, with no Python process anywhere near it. Until 0.6.0, "trained model" meant scikit-learn: pipelines, trees, linear models, all `.fit()` in Python and then turned into a `SELECT` statement. It never covered what a lot of teams are actually training now: PyTorch models, not scikit-learn pipelines.

Orbital 0.6.0 closes that gap. A `torch.nn.Sequential` network, trained exactly the way you already train it, now compiles to the same kind of SQL a linear regression would.

No ONNX Runtime. No model server. No separate inference service to keep alive next to the database. Just a query.

Why does that work at all, for a framework Orbital was never written for? Because of a decision made long before PyTorch was ever on the table.

## Why this isn't a bolt-on

Orbital was never really a scikit-learn tool. Underneath, it converts a scikit-learn pipeline to ONNX (Open Neural Network Exchange, a standard graph format for trained models) using the `skl2onnx` library, then walks that graph node by node to produce SQL. Scikit-learn was always one hop removed from what Orbital actually translates.

Adding PyTorch meant taking the same hop from a different starting point. `torch.onnx.export` turns a `torch.nn.Sequential` model into that same kind of graph. Feed it into the translator that already existed, and the translator doesn't know or care whether the graph came from PyTorch or scikit-learn.

The proof is in how little new code that took. The entire engine for running a feed-forward network in SQL is three small classes: a `Gemm` translator for `Linear` layers, `ReLU`, `Sigmoid`. Everything else (the translator base class, the optimizer, the per-dialect SQL compiler) already existed, built earlier for trees and linear models.

When I first thought of support for PyTorch, I put it this way: *"the underlying translation works on ONNX graphs... the same value proposition orbital already provides for scikit-learn models can apply as it is to pytorch networks exported to ONNX."* That sentence turned out to be the whole implementation plan.

If you want the fuller picture of how a graph becomes SQL, parser, then translator, then optimizer, the [architecture docs](https://posit-dev.github.io/orbital/learnmore/) walk through all three stages in order.

That architecture is also why I keep calling this **multiple frameworks**, not two frameworks. `Relu`, `Sigmoid`, `Tanh`, and `Softmax` are single translators, not one per framework. Scikit-learn's `MLPClassifier` and `MLPRegressor` reach them through `MatMul` and `Add`, PyTorch's `nn.Sequential` reaches the exact same translators through `Gemm`. One implementation, two entry points, and no reason it has to stop at two.

Scikit-learn and PyTorch are both real and shipping today, which is enough on its own to call this "multiple frameworks." But the dependency story is already moving that direction: [issue #113](https://github.com/posit-dev/orbital/issues/113) proposes turning scikit-learn itself into an optional dependency, the same way PyTorch already is, so the core stops assuming any particular framework at all.

## Making it actually usable

Neural networks are layered, and every neuron in layer two reads every output of layer one. If Orbital just inlines those outputs at each place they're read, instead of naming them once, that repetition compounds from one layer to the next. Two layers doubles the inlined text. Five layers is a different order of magnitude.

That's not theoretical: [the issue that tracked the fix](https://github.com/posit-dev/orbital/issues/115) measured scikit-learn's own default `MLPClassifier(hidden_layer_sizes=(100,))`, the first thing anyone reaches for, at 53MB of generated SQL and roughly 894 seconds just to generate it. A hundred neurons in one hidden layer, and the query was already unusable.

PyTorch's `Gemm` translator never had this problem. It has called `preserve()`, materializing its output as a real SQL column, since the day it was written. Scikit-learn's `MLPClassifier` and `MLPRegressor` compile through different ONNX ops though: `MatMul` then `Add`, because that's what `skl2onnx` emits, not `Gemm`. Neither of those translators called `preserve()` at all.

The fix, `Optimizer.preserve_referenced_outputs()`, runs after every single node in the translation loop, for every translator, not just `MatMul` and `Add`, and checks how many times that node's output is actually referenced downstream. Referenced more than once, it gets materialized as a named column. Referenced once or not at all, it stays inlined, no extra column, no extra noise.

None of this is new machinery either. Tree ensembles already lean on the same trick: `preserve()` materializes per-tree votes, or the whole ensemble's aggregated vote so it isn't re-emitted everywhere it's read, as real SQL columns. `preserve_referenced_outputs()` generalizes that same idea automatically, for every translator, whether it's part of an ordinary pipeline or a neural network.

Here's what that fix was worth, measured on three shapes while it was being built:

| Network | Before | After |
|------------------------|------------------------|------------------------|
| `20→64→64→1` (Orbital's own deep-network scaling test) | 12.4MB, ~185s to generate | 234KB |
| `MLPClassifier(hidden_layer_sizes=(100,))`, 3-class (scikit-learn's own default) | 53MB, ~894s to generate | 46.7KB |
| `MLPRegressor(hidden_layer_sizes=(32, 32))` | 1.75MB, ~21s to generate | 57.6KB |

Generation time collapsed just as hard: the `20→64→64→1` network above went from about 185 seconds to about 3.6 seconds. Running the resulting SQL got faster too, if less dramatically: on 200,000 rows, an `MLP(32,32)` query dropped from 0.43s to 0.35s, and an `MLP(100,100)` from 3.58s to 3.31s.

Same hyperparameters. Same defaults everyone actually reaches for. The difference is entirely in how the SQL gets built, not in what the network computes.

## What it can do today

Neural network support in 0.6.0 covers binary classification, multiclass classification, and regression, for both scikit-learn and PyTorch. Five new or updated examples in the repo prove it out: `pytorch_fraud_detector.py`, `pytorch_maintenance_classifier.py`, `pytorch_demand_regressor.py`, `pipeline_mlp_classifier.py`, `pipeline_mlp_regressor.py`.

The one worth walking through is the fraud detector, since it's the shape most teams actually need: a handful of numeric features, a binary "is this fraud" output, trained the same way this kind of model always is.

``` python
FEATURES = {
    "amount": orbital.types.DoubleColumnType(),
    "hour": orbital.types.DoubleColumnType(),
    "v1": orbital.types.DoubleColumnType(),
    "v2": orbital.types.DoubleColumnType(),
}

model = torch.nn.Sequential(
    torch.nn.Linear(len(FEATURES), 16),
    torch.nn.ReLU(),
    torch.nn.Linear(16, 8),
    torch.nn.ReLU(),
    torch.nn.Linear(8, 1),
    torch.nn.Sigmoid(),
)

# ... train model normally: Adam, BCELoss, a plain training loop ...

orbital_pipeline = orbital.parse_pytorch_model(model, FEATURES)
```

From that one `orbital_pipeline`, two engines:

``` python
duckdb_sql = orbital.export_sql("transactions", orbital_pipeline, dialect="duckdb")
postgres_sql = orbital.export_sql("transactions", orbital_pipeline, dialect="postgres")
```

I ran both, against a real DuckDB and a real Postgres, not just read the generated text. Same four test transactions, three ways to compute a prediction (PyTorch itself, the DuckDB query, the Postgres query), and all three agree to within 1e-5. Both queries land around 10KB, not the tens of megabytes a naive translation would have produced before 0.6.0's optimizer fix.

That works because `Sigmoid` and `ReLU` both compile to plain arithmetic: `EXP`, a division, a `CASE WHEN`. Every SQL engine has those. It's not an accident which activation this example uses, either: `Tanh` compiles to a native `TANH()` call instead, and not every dialect implements that the same way, so it's the one activation in Orbital's NN support with an actual portability caveat attached.

DuckDB and Postgres are two of the three dialects [Orbital actively tests in CI](https://posit-dev.github.io/orbital/learnmore/). SQLite is the third. But that's a testing choice, not an architecture boundary: Orbital doesn't write dialect-specific SQL at all. Translation ends at ibis. `export_sql` just hands the finished expression to whichever of ibis's own backend compilers matches the dialect you ask for, and ibis ships about twenty of those: Snowflake, BigQuery, Trino, MySQL, and so on.

## Limits, honestly

What Orbital 0.6.0 handles is feed-forward, fully connected networks: stacks of `Linear` layers with `ReLU`, `Sigmoid`, `Tanh`, or `Softmax` in between. That already covers real use cases people put into production: fraud scoring, churn, demand forecasting, risk models. None of those need a CNN or a transformer.

What it doesn't do yet is exactly what that shape excludes: no convolutions, no recurrence, no attention, no embedding layers for categorical features. If your model needs any of those, Orbital isn't there yet.

SQL size still grows with the network. A few hidden layers of 64 to 128 neurons land comfortably in the KB range. Wider or deeper than that, it's worth checking the generated SQL against whatever statement-size limit your engine has, before you deploy it.

That headroom exists at all thanks to `Optimizer.preserve_referenced_outputs()`, and that mechanism helps every translator in Orbital, not just neural networks. It's a big enough story on its own that I'll get back to in a future post.

## Try it

``` bash
pip install orbital[pytorch]
```

From there, the [getting-started guide](https://posit-dev.github.io/orbital/getstarted/) walks through this same fraud-detector shape end to end, and the [examples directory](https://github.com/posit-dev/orbital/tree/main/examples) has five more, covering classification and regression in both frameworks.

Orbital speaks PyTorch now. Scikit-learn too. Same query either way.

There are more frameworks already in the works. I won't name them here, only that the architecture was built for exactly this.
