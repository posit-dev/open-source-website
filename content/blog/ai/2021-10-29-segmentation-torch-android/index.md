---
title: "Train in R, run on Android: Image segmentation with torch"
description: |
  We train a model for image segmentation in R, using torch together with luz, its high-level interface. We then JIT-trace the model on example input, so as to obtain an optimized representation that can run with no R installed. Finally, we show the model being run on Android.
date: 2021-10-29
categories:
  - Torch
  - Image Recognition & Image Processing
  - R
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.png
ported_from: ai
port_status: in-progress
---



In a sense, image segmentation is not that different from image classification. It's just that instead of categorizing an image as a whole, segmentation results in a label for *every single pixel*. And as in image classification, the categories of interest depend on the task: Foreground versus background, say; different types of tissue; different types of vegetation; et cetera.

The present post is not the first on this blog to treat that topic; and like all prior[^1] ones, it makes use of a U-Net architecture[^2] to achieve its goal. Central characteristics (of this post, not U-Net) are:

1.  It demonstrates how to perform data augmentation for an image segmentation task.

2.  It uses [luz](https://mlverse.github.io/luz/), `torch`'s high-level interface, to train the model.

3.  It [JIT-traces](https://blogs.rstudio.com/ai/posts/2021-08-10-jit-trace-module/) the trained model and saves it for deployment on mobile devices. (JIT being the acronym commonly used for the `torch` just-in-time compiler.)

4.  It includes proof-of-concept code (though not a discussion) of the saved model being run on Android.

And if you think that this in itself is not exciting enough -- our task here is to find cats and dogs. What could be more helpful than a mobile application making sure you can distinguish your cat from the fluffy sofa she's reposing on?

<figure>
<img src="images/Abyssinian_47.jpg" alt="A cat from the Oxford Pet Dataset (Parkhi et al. (2012))." />
<figcaption aria-hidden="true">A cat from the Oxford Pet Dataset (<span class="citation" data-cites="parkhi12a">Parkhi et al. (2012)</span>).</figcaption>
</figure>

## Train in R

We start by preparing the data.

### Pre-processing and data augmentation

As provided by `torchdatasets`, the [Oxford Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/) comes with three variants of target data to choose from: the overall class (cat or dog), the individual breed (there are thirty-seven of them), and a pixel-level segmentation with three categories: foreground, boundary, and background. The latter is the default; and it's exactly the type of target we need.

A call to `oxford_pet_dataset(root = dir)` will trigger the initial download:

``` r
# need torch > 0.6.1
# may have to run remotes::install_github("mlverse/torch", ref = remotes::github_pull("713")) depending on when you read this
library(torch) 
library(torchvision)
library(torchdatasets)
library(luz)

dir <- "~/.torch-datasets/oxford_pet_dataset"

ds <- oxford_pet_dataset(root = dir)
```

Images (and corresponding masks) come in different sizes. For training, however, we'll need all of them to be the same size. This can be accomplished by passing in `transform =` and `target_transform =` arguments. But what about data augmentation (basically always a useful measure to take)? Imagine we make use of random flipping. An input image will be flipped -- or not -- according to some probability. But if the image is flipped, the mask better had be, as well! Input and target transformations are not independent, in this case.

A solution is to create a wrapper around `oxford_pet_dataset()` that lets us "hook into" the `.getitem()` method, like so:

``` r
pet_dataset <- torch::dataset(
  
  inherit = oxford_pet_dataset,
  
  initialize = function(..., size, normalize = TRUE, augmentation = NULL) {
    
    self$augmentation <- augmentation
    
    input_transform <- function(x) {
      x <- x %>%
        transform_to_tensor() %>%
        transform_resize(size) 
      # we'll make use of pre-trained MobileNet v2 as a feature extractor
      # => normalize in order to match the distribution of images it was trained with
      if (isTRUE(normalize)) x <- x %>%
        transform_normalize(mean = c(0.485, 0.456, 0.406),
                            std = c(0.229, 0.224, 0.225))
      x
    }
    
    target_transform <- function(x) {
      x <- torch_tensor(x, dtype = torch_long())
      x <- x[newaxis,..]
      # interpolation = 0 makes sure we still end up with integer classes
      x <- transform_resize(x, size, interpolation = 0)
    }
    
    super$initialize(
      ...,
      transform = input_transform,
      target_transform = target_transform
    )
    
  },
  .getitem = function(i) {
    
    item <- super$.getitem(i)
    if (!is.null(self$augmentation)) 
      self$augmentation(item)
    else
      list(x = item$x, y = item$y[1,..])
  }
)
```

All we have to do now is create a custom function that lets us decide on what augmentation to apply to each input-target pair, and then, manually call the respective transformation functions.

Here, we flip, on average, every second image, and if we do, we flip the mask as well. The second transformation -- orchestrating random changes in brightness, saturation, and contrast -- is applied to the input image only.

``` r
augmentation <- function(item) {
  
  vflip <- runif(1) > 0.5
  
  x <- item$x
  y <- item$y
  
  if (isTRUE(vflip)) {
    x <- transform_vflip(x)
    y <- transform_vflip(y)
  }
  
  x <- transform_color_jitter(x, brightness = 0.5, saturation = 0.3, contrast = 0.3)
  
  list(x = x, y = y[1,..])
  
}
```

We now make use of the wrapper, `pet_dataset()`, to instantiate the training and validation sets, and create the respective data loaders.

``` r
train_ds <- pet_dataset(root = dir,
                        split = "train",
                        size = c(224, 224),
                        augmentation = augmentation)
valid_ds <- pet_dataset(root = dir,
                        split = "valid",
                        size = c(224, 224))

train_dl <- dataloader(train_ds, batch_size = 32, shuffle = TRUE)
valid_dl <- dataloader(valid_ds, batch_size = 32)
```

### Model definition

The model implements a classic U-Net architecture, with an encoding stage (the "down" pass), a decoding stage (the "up" pass), and importantly, a "bridge" that passes features preserved from the encoding stage on to corresponding layers in the decoding stage.

#### Encoder

First, we have the encoder. It uses a pre-trained model (MobileNet v2) as its feature extractor.

The encoder splits up MobileNet v2's feature extraction blocks into several stages, and applies one stage after the other. Respective results are saved in a list.

``` r
encoder <- nn_module(
  
  initialize = function() {
    model <- model_mobilenet_v2(pretrained = TRUE)
    self$stages <- nn_module_list(list(
      nn_identity(),
      model$features[1:2],
      model$features[3:4],
      model$features[5:7],
      model$features[8:14],
      model$features[15:18]
    ))

    for (par in self$parameters) {
      par$requires_grad_(FALSE)
    }

  },
  forward = function(x) {
    features <- list()
    for (i in 1:length(self$stages)) {
      x <- self$stages[[i]](x)
      features[[length(features) + 1]] <- x
    }
    features
  }
)
```

#### Decoder

The decoder is made up of configurable blocks. A block receives two input tensors: one that is the result of applying the previous decoder block, and one that holds the feature map produced in the matching encoder stage. In the forward pass, first the former is upsampled, and passed through a nonlinearity. The intermediate result is then prepended to the second argument, the channeled-through feature map. On the resultant tensor, a convolution is applied, followed by another nonlinearity.

``` r
decoder_block <- nn_module(
  
  initialize = function(in_channels, skip_channels, out_channels) {
    self$upsample <- nn_conv_transpose2d(
      in_channels = in_channels,
      out_channels = out_channels,
      kernel_size = 2,
      stride = 2
    )
    self$activation <- nn_relu()
    self$conv <- nn_conv2d(
      in_channels = out_channels + skip_channels,
      out_channels = out_channels,
      kernel_size = 3,
      padding = "same"
    )
  },
  forward = function(x, skip) {
    x <- x %>%
      self$upsample() %>%
      self$activation()

    input <- torch_cat(list(x, skip), dim = 2)

    input %>%
      self$conv() %>%
      self$activation()
  }
)
```

The decoder itself "just" instantiates and runs through the blocks:

``` r
decoder <- nn_module(
  
  initialize = function(
    decoder_channels = c(256, 128, 64, 32, 16),
    encoder_channels = c(16, 24, 32, 96, 320)
  ) {

    encoder_channels <- rev(encoder_channels)
    skip_channels <- c(encoder_channels[-1], 3)
    in_channels <- c(encoder_channels[1], decoder_channels)

    depth <- length(encoder_channels)

    self$blocks <- nn_module_list()
    for (i in seq_len(depth)) {
      self$blocks$append(decoder_block(
        in_channels = in_channels[i],
        skip_channels = skip_channels[i],
        out_channels = decoder_channels[i]
      ))
    }

  },
  forward = function(features) {
    features <- rev(features)
    x <- features[[1]]
    for (i in seq_along(self$blocks)) {
      x <- self$blocks[[i]](x, features[[i+1]])
    }
    x
  }
)
```

#### Top-level module

Finally, the top-level module generates the class score. In our task, there are three pixel classes. The score-producing submodule can then just be a final convolution, producing three channels:

``` r
model <- nn_module(
  
  initialize = function() {
    self$encoder <- encoder()
    self$decoder <- decoder()
    self$output <- nn_sequential(
      nn_conv2d(in_channels = 16,
                out_channels = 3,
                kernel_size = 3,
                padding = "same")
    )
  },
  forward = function(x) {
    x %>%
      self$encoder() %>%
      self$decoder() %>%
      self$output()
  }
)
```

### Model training and (visual) evaluation

With `luz`, model training is a matter of two verbs, `setup()` and `fit()`. The learning rate has been determined, for this specific case, using `luz::lr_finder()`; you will likely have to change it when experimenting with different forms of data augmentation (and different data sets).

``` r
model <- model %>%
  setup(optimizer = optim_adam, loss = nn_cross_entropy_loss())

fitted <- model %>%
  set_opt_hparams(lr = 1e-3) %>%
  fit(train_dl, epochs = 10, valid_data = valid_dl)
```

Here is an excerpt of how training performance developed in my case:

    # Epoch 1/10
    # Train metrics: Loss: 0.504                                                           
    # Valid metrics: Loss: 0.3154

    # Epoch 2/10
    # Train metrics: Loss: 0.2845                                                           
    # Valid metrics: Loss: 0.2549

    ...
    ...

    # Epoch 9/10
    # Train metrics: Loss: 0.1368                                                           
    # Valid metrics: Loss: 0.2332

    # Epoch 10/10
    # Train metrics: Loss: 0.1299                                                           
    # Valid metrics: Loss: 0.2511

Numbers are just numbers -- how good is the trained model really at segmenting pet images? To find out, we generate segmentation masks for the first eight observations in the validation set, and plot them overlaid on the images. A convenient way to plot an image and superimpose a mask is provided by the `raster` package.

``` r
library(raster)
```

Pixel intensities have to be between zero and one, which is why in the dataset wrapper, we have made it so normalization can be switched off. To plot the actual images, we just instantiate a clone of `valid_ds` that leaves the pixel values unchanged. (The predictions, on the other hand, will still have to be obtained from the original validation set.)

``` r
valid_ds_4plot <- pet_dataset(
  root = dir,
  split = "valid",
  size = c(224, 224),
  normalize = FALSE
)
```

Finally, the predictions are generated in a loop, and overlaid over the images one-by-one:

``` r
indices <- 1:8

preds <- predict(fitted, dataloader(dataset_subset(valid_ds, indices)))

png("pet_segmentation.png", width = 1200, height = 600, bg = "black")

par(mfcol = c(2, 4), mar = rep(2, 4))

for (i in indices) {
  
  mask <- as.array(torch_argmax(preds[i,..], 1)$to(device = "cpu"))
  mask <- raster::ratify(raster::raster(mask))
  
  img <- as.array(valid_ds_4plot[i][[1]]$permute(c(2,3,1)))
  cond <- img > 0.99999
  img[cond] <- 0.99999
  img <- raster::brick(img)
  
  # plot image
  raster::plotRGB(img, scale = 1, asp = 1, margins = TRUE)
  # overlay mask
  plot(mask, alpha = 0.4, legend = FALSE, axes = FALSE, add = TRUE)
  
}
```

<figure>
<img src="images/pet_segmentation.png" alt="Learned segmentation masks, overlaid on images from the validation set." />
<figcaption aria-hidden="true">Learned segmentation masks, overlaid on images from the validation set.</figcaption>
</figure>

Now onto running this model "in the wild" (well, sort of).

## JIT-trace and run on Android

Tracing the trained model will convert it to a form that can be loaded in R-less environments -- for example, from Python, C++, or Java.

<aside>

Please see our [introduction to the torch JIT compiler](https://blogs.rstudio.com/ai/posts/2021-08-10-jit-trace-module/).

</aside>

We access the `torch` model underlying the fitted `luz` object, and trace it -- where tracing means calling it once, on a sample observation:

``` r
m <- fitted$model
x <- coro::collect(train_dl, 1)

traced <- jit_trace(m, x[[1]]$x)
```

The traced model could now be saved for use with Python or C++, like so:

``` r
traced %>% jit_save("traced_model.pt")
```

However, since we already know we'd like to deploy it on Android, we instead make use of the specialized function `jit_save_for_mobile()` that, additionally, generates bytecode:

``` r
# need torch > 0.6.1
jit_save_for_mobile(traced_model, "model_bytecode.pt")
```

And that's it for the R side!

For running on Android, I made heavy use of PyTorch Mobile's Android [example apps](https://github.com/pytorch/android-demo-app), especially the [image segmentation](https://github.com/pytorch/android-demo-app/tree/master/ImageSegmentation) one.

The actual proof-of-concept code for this post (which was used to generate the below picture) may be found here: <https://github.com/skeydan/ImageSegmentation>. (Be warned though -- it's my first Android application!).

Of course, we still have to try to find the cat. Here is the model, run on a device emulator in Android Studio, on three images (from the Oxford Pet Dataset) selected for, firstly, a wide range in difficulty, and secondly, well ... for cuteness:

<figure>
<img src="images/segmentation_android.png" alt="Where’s my cat?" />
<figcaption aria-hidden="true">Where’s my cat?</figcaption>
</figure>

Thanks for reading!

Parkhi, Omkar M., Andrea Vedaldi, Andrew Zisserman, and C. V. Jawahar. 2012. "Cats and Dogs." *IEEE Conference on Computer Vision and Pattern Recognition*.

Ronneberger, Olaf, Philipp Fischer, and Thomas Brox. 2015. "U-Net: Convolutional Networks for Biomedical Image Segmentation." *CoRR* abs/1505.04597. <http://arxiv.org/abs/1505.04597>.

[^1]: Cf. [Brain image segmentation with torch](https://blogs.rstudio.com/ai/posts/2020-11-30-torch-brain-segmentation/) (using, non-surprisingly, `torch`), and [Image segmentation with U-Net](https://blogs.rstudio.com/ai/posts/2019-08-23-unet/) (using TensorFlow/Keras).

[^2]: Ronneberger et al. (2015)
