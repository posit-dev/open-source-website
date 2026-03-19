---
title: "luz 0.3.0"
description: |
  luz version 0.3.0 is now on CRAN. luz is a high-level interface for torch.
date: 2022-08-24T00:00:00.000Z
slug: luz-0-3-0
categories:
  - Torch
  - Packages/Releases
  - R
author:
  - name: Daniel Falbel
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Daniel Falbel
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
---



We are happy to announce that `luz` version 0.3.0 is now on CRAN. This
release brings a few improvements to the learning rate finder
first contributed by [Chris
McMaster](https://github.com/cmcmaster1). As we didn't have a
0.2.0 release post, we will also highlight a few improvements that
date back to that version.

## What's `luz`?

Since it is [relatively new
package](/blog/ai/2021-06-17-luz/), we are
starting this blog post with a quick recap of how `luz` works. If you
already know what `luz` is, feel free to move on to the next section.

`luz` is a high-level API for `torch` that aims to encapsulate the training
loop into a set of reusable pieces of code. It reduces the boilerplate
required to train a model with `torch`, avoids the error-prone
`zero_grad()` - `backward()` - `step()` sequence of calls, and also
simplifies the process of moving data and models between CPUs and GPUs.

With `luz` you can take your `torch` `nn_module()`, for example the
two-layer perceptron defined below:

``` r
modnn <- nn_module(
  initialize = function(input_size) {
    self$hidden <- nn_linear(input_size, 50)
    self$activation <- nn_relu()
    self$dropout <- nn_dropout(0.4)
    self$output <- nn_linear(50, 1)
  },
  forward = function(x) {
    x %>% 
      self$hidden() %>% 
      self$activation() %>% 
      self$dropout() %>% 
      self$output()
  }
)
```

and fit it to a specified dataset like so:

``` r
fitted <- modnn %>% 
  setup(
    loss = nn_mse_loss(),
    optimizer = optim_rmsprop,
    metrics = list(luz_metric_mae())
  ) %>% 
  set_hparams(input_size = 50) %>% 
  fit(
    data = list(x_train, y_train),
    valid_data = list(x_valid, y_valid),
    epochs = 20
  )
```

`luz` will automatically train your model on the GPU if it's available,
display a nice progress bar during training, and handle logging of metrics,
all while making sure evaluation on validation data is performed in the correct way
(e.g., disabling dropout).

`luz` can be extended in many different layers of abstraction, so you can
improve your knowledge gradually, as you need more advanced features in your
project. For example, you can implement [custom
metrics](https://mlverse.github.io/luz/reference/luz_metric.html),
[callbacks](https://mlverse.github.io/luz/reference/luz_callback.html),
or even customize the [internal training
loop](https://mlverse.github.io/luz/articles/custom-loop.html).

To learn about `luz`, read the [getting
started](https://mlverse.github.io/luz/articles/get-started.html)
section on the website, and browse the [examples
gallery](https://mlverse.github.io/luz/articles/examples/index.html).

## What's new in `luz`?

### Learning rate finder

In deep learning, finding a good learning rate is essential to be able
to fit your model. If it's too low, you will need too many iterations
for your loss to converge, and that might be impractical if your model
takes too long to run. If it's too high, the loss can explode and you
might never be able to arrive at a minimum.

The `lr_finder()` function implements the algorithm detailed in [Cyclical Learning Rates for
Training Neural Networks](https://arxiv.org/abs/1506.01186)
(Smith 2015) popularized in the FastAI framework (Howard and Gugger 2020). It
takes an `nn_module()` and some data to produce a data frame with the
losses and the learning rate at each step.

``` r
model <- net %>% setup(
  loss = torch::nn_cross_entropy_loss(),
  optimizer = torch::optim_adam
)

records <- lr_finder(
  object = model, 
  data = train_ds, 
  verbose = FALSE,
  dataloader_options = list(batch_size = 32),
  start_lr = 1e-6, # the smallest value that will be tried
  end_lr = 1 # the largest value to be experimented with
)

str(records)
#> Classes 'lr_records' and 'data.frame':   100 obs. of  2 variables:
#>  $ lr  : num  1.15e-06 1.32e-06 1.51e-06 1.74e-06 2.00e-06 ...
#>  $ loss: num  2.31 2.3 2.29 2.3 2.31 ...
```

You can use the built-in plot method to display the exact results, along
with an exponentially smoothed value of the loss.

``` r
plot(records) +
  ggplot2::coord_cartesian(ylim = c(NA, 5))
```

<figure>
<img src="images/lr-finder.png" alt="Plot displaying the results of the lr_finder()" />
<figcaption aria-hidden="true">Plot displaying the results of the lr_finder()</figcaption>
</figure>

If you want to learn how to interpret the results of this plot and learn
more about the methodology read the [learning rate finder
article](https://mlverse.github.io/luz/articles/lr-finder.html) on the
`luz` website.

### Data handling

In the first release of `luz`, the only kind of object that was allowed to
be used as input data to `fit` was a `torch` `dataloader()`. As of version
0.2.0, `luz` also support's R matrices/arrays (or nested lists of them) as
input data, as well as `torch` `dataset()`s.

Supporting low level abstractions like `dataloader()` as input data is
important, as with them the user has full control over how input
data is loaded. For example, you can create parallel dataloaders,
change how shuffling is done, and more. However, having to manually
define the dataloader seems unnecessarily tedious when you don't need to
customize any of this.

Another small improvement from version 0.2.0, inspired by Keras, is that
you can pass a value between 0 and 1 to `fit`'s `valid_data` parameter, and `luz` will
take a random sample of that proportion from the training set, to be used for
validation data.

Read more about this in the documentation of the
[`fit()`](https://mlverse.github.io/luz/reference/fit.luz_module_generator.html#arguments)
function.

### New callbacks

In recent releases, new built-in callbacks were added to `luz`:

- `luz_callback_gradient_clip()`: Helps avoiding loss divergence by
  clipping large gradients.
- `luz_callback_keep_best_model()`: Each epoch, if there's improvement
  in the monitored metric, we serialize the model weights to a temporary
  file. When training is done, we reload weights from the best model.
- `luz_callback_mixup()`: Implementation of ['mixup: Beyond Empirical
  Risk Minimization'](https://arxiv.org/abs/1710.09412)
  (Zhang et al. 2017). Mixup is a nice data augmentation technique that
  helps improving model consistency and overall performance.

## Final remarks

You can see the full changelog available
[here](https://mlverse.github.io/luz/news/index.html).

In this post we would also like to thank:

- [@jonthegeek](https://github.com/jonthegeek) for valuable
  improvements in the `luz` getting-started guides.

- [@mattwarkentin](https://github.com/mattwarkentin) for many good
  ideas, improvements and bug fixes.

- [@cmcmaster1](https://github.com/cmcmaster1) for the initial
  implementation of the learning rate finder and other bug fixes.

- [@skeydan](https://github.com/skeydan) for the implementation of the Mixup callback and improvements in the learning rate finder.

Thank you!

Photo by <a href="https://unsplash.com/@visualsbydil?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dil</a> on <a href="https://unsplash.com/s/photos/light-bulb?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Howard, Jeremy, and Sylvain Gugger. 2020. "Fastai: A Layered API for Deep Learning." *Information* 11 (2): 108. <https://doi.org/10.3390/info11020108>.

Smith, Leslie N. 2015. *Cyclical Learning Rates for Training Neural Networks*. <https://doi.org/10.48550/ARXIV.1506.01186>.

Zhang, Hongyi, Moustapha Cisse, Yann N. Dauphin, and David Lopez-Paz. 2017. *Mixup: Beyond Empirical Risk Minimization*. <https://doi.org/10.48550/ARXIV.1710.09412>.
