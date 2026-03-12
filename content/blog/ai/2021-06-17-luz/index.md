---
title: "Que haja luz: More light for torch!"
description: |
  Today, we're introducing luz, a high-level interface to torch that lets you train neural networks in a concise, declarative style. In some sense, it is to torch what Keras is to TensorFlow: It provides both a streamlined workflow and powerful ways for customization.
date: 2021-06-17
categories:
  - Torch
  - R
  - Packages/Releases
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: raw
---



*... Before we start, my apologies to our Spanish-speaking readers ... I had to make a choice between "haja"*[^1] *and "haya"*[^2]*, and in the end it was all up to a coin flip ...*

As I write this, we're more than happy with the rapid adoption we've seen of `torch` -- not just for immediate use, but also, in packages that build on it, making use of its core functionality.

In an applied scenario, though -- a scenario that involves training and validating in lockstep, computing metrics and acting on them, and dynamically changing hyper-parameters during the process -- it may sometimes seem like there's a non-negligible amount of boilerplate code involved. For one, there is the main loop over epochs, and inside, the loops over training and validation batches. Furthermore, steps like updating the model's *mode* (training or validation, resp.), zeroing out and computing gradients, and propagating back model updates have to be performed in the correct order. Last not least, care has to be taken that at any moment, tensors are located on the expected *device*.

*Wouldn't it be dreamy if*, as the popular-in-the-early-2000s "Head First ..."[^3] series used to say, there was a way to eliminate those manual steps, while keeping the flexibility? With `luz`, there is.

In this post, our focus is on two things: First of all, the streamlined workflow itself; and second, generic mechanisms that allow for customization. For more detailed examples of the latter, plus concrete coding instructions, we will link to the (already-extensive) documentation.

## Train and validate, then test: A basic deep-learning workflow with `luz`

To demonstrate the essential workflow, we make use of a dataset that's readily available and won't distract us too much, pre-processing-wise: namely, the *Dogs vs. Cats* collection that comes with `torchdatasets`. `torchvision` will be needed for image transformations; apart from those two packages all we need are `torch` and `luz`.

``` r
# all these are available on CRAN
library(torch)
library(torchvision)
library(torchdatasets)
library(luz)
```

#### Data

The dataset is downloaded from Kaggle; you'll need to edit the path below to reflect the location of your own Kaggle token.

``` r
dir <- "~/Downloads/dogs-vs-cats" 

ds <- torchdatasets::dogs_vs_cats_dataset(
  dir,
  token = "~/.kaggle/kaggle.json",
  transform = . %>%
    torchvision::transform_to_tensor() %>%
    torchvision::transform_resize(size = c(224, 224)) %>% 
    torchvision::transform_normalize(rep(0.5, 3), rep(0.5, 3)),
  target_transform = function(x) as.double(x) - 1
)
```

Conveniently, we can use `dataset_subset()` to partition the data into training, validation, and test sets.

``` r
train_ids <- sample(1:length(ds), size = 0.6 * length(ds))
valid_ids <- sample(setdiff(1:length(ds), train_ids), size = 0.2 * length(ds))
test_ids <- setdiff(1:length(ds), union(train_ids, valid_ids))

train_ds <- dataset_subset(ds, indices = train_ids)
valid_ds <- dataset_subset(ds, indices = valid_ids)
test_ds <- dataset_subset(ds, indices = test_ids)
```

Next, we instantiate the respective `dataloader`s.

``` r
train_dl <- dataloader(train_ds, batch_size = 64, shuffle = TRUE, num_workers = 4)
valid_dl <- dataloader(valid_ds, batch_size = 64, num_workers = 4)
test_dl <- dataloader(test_ds, batch_size = 64, num_workers = 4)
```

That's it for the data -- no change in workflow so far. Neither is there a difference in how we define the model.

#### Model

To speed up training, we build on pre-trained AlexNet ( Krizhevsky (2014)).

``` r
net <- torch::nn_module(
  
  initialize = function(output_size) {
    self$model <- model_alexnet(pretrained = TRUE)

    for (par in self$parameters) {
      par$requires_grad_(FALSE)
    }

    self$model$classifier <- nn_sequential(
      nn_dropout(0.5),
      nn_linear(9216, 512),
      nn_relu(),
      nn_linear(512, 256),
      nn_relu(),
      nn_linear(256, output_size)
    )
  },
  forward = function(x) {
    self$model(x)[,1]
  }
  
)
```

If you look closely, you see that all we've done so far is *define* the model. Unlike in a `torch`-only workflow, we are not going to instantiate it, and neither are we going to move it to an eventual GPU.

Expanding on the latter, we can say more: *All* of device handling is managed by `luz`. It probes for existence of a CUDA-capable GPU, and if it finds one, makes sure both model weights and data tensors are moved there transparently whenever needed. The same goes for the opposite direction: Predictions computed on the test set, for example, are silently transferred to the CPU, ready for the user to further manipulate them in R. But as to predictions, we're not quite there yet: On to model training, where the difference made by `luz` jumps right to the eye.

#### Training

Below, you see four calls to `luz`, two of which are required in every setting, and two are case-dependent. The always-needed ones are `setup()` and `fit()` :

- In `setup()`, you tell `luz` what the loss should be, and which optimizer to use. Optionally, beyond the loss itself (the primary metric, in a sense, in that it informs weight updating) you can have `luz` compute additional ones. Here, for example, we ask for classification accuracy. (For a human watching a progress bar, a two-class accuracy of 0.91 is way more indicative than cross-entropy loss of 1.26.)

- In `fit()`, you pass references to the training and validation `dataloader`s. Although a default exists for the number of epochs to train for, you'll normally want to pass a custom value for this parameter, too.

The case-dependent calls here, then, are those to `set_hparams()` and `set_opt_hparams()`. Here,

- `set_hparams()` appears because, in the model definition, we had `initialize()` take a parameter, `output_size`. Any arguments expected by `initialize()` need to be passed via this method.

- `set_opt_hparams()` is there because we want to use a non-default learning rate with `optim_adam()`. Were we content with the default, no such call would be in order.

``` r
fitted <- net %>%
  setup(
    loss = nn_bce_with_logits_loss(),
    optimizer = optim_adam,
    metrics = list(
      luz_metric_binary_accuracy_with_logits()
    )
  ) %>%
  set_hparams(output_size = 1) %>%
  set_opt_hparams(lr = 0.01) %>%
  fit(train_dl, epochs = 3, valid_data = valid_dl)
```

Here's how the output looked for me:

``` r
Epoch 1/3
Train metrics: Loss: 0.8692 - Acc: 0.9093
Valid metrics: Loss: 0.1816 - Acc: 0.9336
Epoch 2/3
Train metrics: Loss: 0.1366 - Acc: 0.9468
Valid metrics: Loss: 0.1306 - Acc: 0.9458
Epoch 3/3
Train metrics: Loss: 0.1225 - Acc: 0.9507
Valid metrics: Loss: 0.1339 - Acc: 0.947
```

Training finished, we can ask `luz` to save the trained model:

``` r
luz_save(fitted, "dogs-and-cats.pt")
```

#### Test set predictions

And finally, `predict()` will obtain predictions on the data pointed to by a passed-in `dataloader` -- here, the test set. It expects a fitted model as its first argument.

``` r
preds <- predict(fitted, test_dl)

probs <- torch_sigmoid(preds)
print(probs, n = 5)
```

    torch_tensor
     1.2959e-01
     1.3032e-03
     6.1966e-05
     5.9575e-01
     4.5577e-03
    ... [the output was truncated (use n=-1 to disable)]
    [ CPUFloatType{5000} ]

And that's it for a complete workflow. In case you have prior experience with Keras, this should feel pretty familiar. The same can be said for the most versatile-yet-standardized customization technique implemented in `luz`.

## How to do (almost) anything (almost) anytime

Like Keras, `luz` has the concept of *callbacks* that can "hook into" the training process and execute arbitrary R code. Specifically, code can be scheduled to run at any of the following points in time:

- when the overall training process starts or ends (`on_fit_begin()` / `on_fit_end()`);

- when an epoch of training plus validation starts or ends (`on_epoch_begin()` / `on_epoch_end()`);

- when during an epoch, the training (validation, resp.) half starts or ends (`on_train_begin()` / `on_train_end()`; `on_valid_begin()` / `on_valid_end()`);

- when during training (validation, resp.) a new batch is either about to, or has been processed (`on_train_batch_begin()` / `on_train_batch_end()`; `on_valid_batch_begin()` / `on_valid_batch_end()`);

- and even at specific landmarks inside the "innermost" training / validation logic, such as "after loss computation", "after backward", or "after step".

While you can implement any logic you wish using this technique, `luz` already comes equipped with a very useful set of callbacks.

<aside>
See the main vignette, [Getting started with luz](https://mlverse.github.io/luz/articles/get-started.html), for instructions on how to create callback objects.
</aside>

For example:

- `luz_callback_model_checkpoint()` periodically saves model weights.

- `luz_callback_lr_scheduler()` allows to activate one of `torch`'s *learning rate schedulers*. Different schedulers exist, each following their own logic in how they dynamically adjust the learning rate.

- `luz_callback_early_stopping()` terminates training once model performance stops improving.

Callbacks are passed to `fit()` in a list. Here we adapt our above example, making sure that (1) model weights are saved after each epoch and (2), training terminates if validation loss does not improve for two epochs in a row.

``` r
fitted <- net %>%
  setup(
    loss = nn_bce_with_logits_loss(),
    optimizer = optim_adam,
    metrics = list(
      luz_metric_binary_accuracy_with_logits()
    )
  ) %>%
  set_hparams(output_size = 1) %>%
  set_opt_hparams(lr = 0.01) %>%
  fit(train_dl,
      epochs = 10,
      valid_data = valid_dl,
      callbacks = list(luz_callback_model_checkpoint(path = "./models"),
                       luz_callback_early_stopping(patience = 2)))
```

What about other types of flexibility requirements -- such as in the scenario of multiple, interacting models, equipped, each, with their own loss functions and optimizers[^4]? In such cases, the code will get a bit longer than what we've been seeing here, but `luz` can still help considerably with streamlining the workflow.

<aside>
Several alternatives, trading off control and convenience, are discussed in the [Custom loops](https://mlverse.github.io/luz/articles/custom-loop.html) and [Accelerator](https://mlverse.github.io/luz/articles/accelerator.html) vignettes.
</aside>

To conclude, using `luz`, you lose nothing of the flexibility that comes with `torch`, while gaining a lot in code simplicity, modularity, and maintainability. We'd be happy to hear you'll give it a try!

Thanks for reading!

Photo by <a href="https://unsplash.com/@jdrincs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">JD Rincs</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Krizhevsky, Alex. 2014. "One Weird Trick for Parallelizing Convolutional Neural Networks." *CoRR* abs/1404.5997. <http://arxiv.org/abs/1404.5997>.

[^1]: Portuguese

[^2]: Spanish

[^3]: A well-known (at the time) exemplar having been, e.g., "Head First Design Patterns", by Freeman et al..

[^4]: Think GANs (*Generative Adversarial Networks*), a popular architecture rooted in game-theoretic concepts.
