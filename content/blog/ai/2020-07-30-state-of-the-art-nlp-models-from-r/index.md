---
title: "State-of-the-art NLP models from R"
description: >
  Nowadays, Microsoft, Google, Facebook, and OpenAI are sharing lots of
  state-of-the-art models in the field of Natural Language Processing. However,
  fewer materials exist how to use these models from R. In this post, we will
  show how R users can access and benefit from these models as well.
date: 2020-07-30
categories:
  - Natural Language Processing
author:
  - name: Turgut Abdullayev
    url: https://github.com/henry090
    affiliation: QSS Analytics
    affiliation_url: http://www.qss.az/
people:
  - Turgut Abdullayev
image: thumbnail.jpg
ported_from: ai
port_status: raw
---



<link href="state-of-the-art-nlp-models-from-r_files/libs/htmltools-fill-0.5.9/fill.css" rel="stylesheet" />
<script src="state-of-the-art-nlp-models-from-r_files/libs/htmlwidgets-1.6.4/htmlwidgets.js"></script>
<link href="state-of-the-art-nlp-models-from-r_files/libs/datatables-css-0.0.0/datatables-crosstalk.css" rel="stylesheet" />
<script src="state-of-the-art-nlp-models-from-r_files/libs/datatables-binding-0.34.0/datatables.js"></script>
<script src="state-of-the-art-nlp-models-from-r_files/libs/jquery-3.6.0/jquery-3.6.0.min.js"></script>
<link href="state-of-the-art-nlp-models-from-r_files/libs/dt-core-1.13.6/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="state-of-the-art-nlp-models-from-r_files/libs/dt-core-1.13.6/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="state-of-the-art-nlp-models-from-r_files/libs/dt-core-1.13.6/js/jquery.dataTables.min.js"></script>
<link href="state-of-the-art-nlp-models-from-r_files/libs/crosstalk-1.2.2/css/crosstalk.min.css" rel="stylesheet" />
<script src="state-of-the-art-nlp-models-from-r_files/libs/crosstalk-1.2.2/js/crosstalk.min.js"></script>


<style type="text/css">
.colab-root {
    display: inline-block;
    background: rgba(255, 255, 255, 0.75);
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 11px!important;
    text-decoration: none;
    color: #aaa;
    border: none;
    font-weight: 300;
    border: solid 1px rgba(0, 0, 0, 0.08);
    border-bottom-color: rgba(0, 0, 0, 0.15);
    text-transform: uppercase;
    line-height: 16px;
}
span.colab-span {
    background-image: url(https://www.vectorlogo.zone/logos/kaggle/kaggle-ar21.svg);
    background-repeat: no-repeat;
    background-size: 51px;
    background-position-y: -4px;
    display: inline-block;
    padding-left: 24px;
    border-radius: 4px;
    text-decoration: none;
}
</style>

## Introduction

The *Transformers* repository from ["Hugging Face"](https://github.com/huggingface/transformers) contains a lot of ready to use, state-of-the-art models, which are straightforward to download and fine-tune with Tensorflow & Keras.

For this purpose the users usually need to get:

- The model itself (e.g. Bert, Albert, RoBerta, GPT-2 and etc.)
- The tokenizer object
- The weights of the model

In this post, we will work on a classic binary classification task and train our dataset on 3 models:

- [GPT-2](https://blog.openai.com/better-language-models/) from Open AI
- [RoBERTa](https://arxiv.org/abs/1907.11692) from Facebook
- [Electra](https://arxiv.org/abs/2003.10555) from Google Research/Stanford University

However, readers should know that one can work with transformers on a variety of down-stream tasks, such as:

1.  feature extraction
2.  sentiment analysis
3.  [text classification](https://github.com/huggingface/transformers/tree/master/examples/text-classification)
4.  [question answering](https://github.com/huggingface/transformers/tree/master/examples/question-answering)
5.  [summarization](https://github.com/huggingface/transformers/tree/master/examples/seq2seq)
6.  [translation](https://github.com/huggingface/transformers/tree/master/examples/seq2seq) and [many more](https://github.com/huggingface/transformers/tree/master/examples).

## Prerequisites

Our first job is to install the *transformers* package via `reticulate`.

``` r
reticulate::py_install('transformers', pip = TRUE)
```

Then, as usual, load standard 'Keras', 'TensorFlow' \>= 2.0 and some classic libraries from R.

``` r
library(keras)
library(tensorflow)
library(dplyr)
library(tfdatasets)

transformer = reticulate::import('transformers')
```

Note that if running TensorFlow on GPU one could specify the following parameters in order to avoid memory issues.

``` r
physical_devices = tf$config$list_physical_devices('GPU')
tf$config$experimental$set_memory_growth(physical_devices[[1]],TRUE)

tf$keras$backend$set_floatx('float32')
```

## Template

We already mentioned that to train a data on the specific model, users should download the model, its tokenizer object and weights. For example, to get a RoBERTa model one has to do the following:

``` r
# get Tokenizer
transformer$RobertaTokenizer$from_pretrained('roberta-base', do_lower_case=TRUE)

# get Model with weights
transformer$TFRobertaModel$from_pretrained('roberta-base')
```

## Data preparation

A dataset for binary classification is provided in [text2vec](http://text2vec.org/) package. Let's load the dataset and take a sample for fast model training.

``` r
library(text2vec)
data("movie_review")
df = movie_review %>% rename(target = sentiment, comment_text = review) %>% 
  sample_n(2000) %>% 
  data.table::as.data.table()
```

Split our data into 2 parts:

``` r
idx_train = sample.int(nrow(df)*0.8)

train = df[idx_train,]
test = df[!idx_train,]
```

## Data input for Keras

Until now, we've just covered data import and train-test split. To feed input to the network we have to turn our raw text into indices via the imported tokenizer. And then adapt the model to do binary classification by adding a dense layer with a single unit at the end.

However, we want to train our data for 3 models GPT-2, RoBERTa, and Electra. We need to write a loop for that.

> Note: one model in general requires 500-700 MB

``` r
# list of 3 models
ai_m = list(
  c('TFGPT2Model',       'GPT2Tokenizer',       'gpt2'),
   c('TFRobertaModel',    'RobertaTokenizer',    'roberta-base'),
   c('TFElectraModel',    'ElectraTokenizer',    'google/electra-small-generator')
)

# parameters
max_len = 50L
epochs = 2
batch_size = 10

# create a list for model results
gather_history = list()

for (i in 1:length(ai_m)) {
  
  # tokenizer
  tokenizer = glue::glue("transformer${ai_m[[i]][2]}$from_pretrained('{ai_m[[i]][3]}',
                         do_lower_case=TRUE)") %>% 
    rlang::parse_expr() %>% eval()
  
  # model
  model_ = glue::glue("transformer${ai_m[[i]][1]}$from_pretrained('{ai_m[[i]][3]}')") %>% 
    rlang::parse_expr() %>% eval()
  
  # inputs
  text = list()
  # outputs
  label = list()
  
  data_prep = function(data) {
    for (i in 1:nrow(data)) {
      
      txt = tokenizer$encode(data[['comment_text']][i],max_length = max_len, 
                             truncation=T) %>% 
        t() %>% 
        as.matrix() %>% list()
      lbl = data[['target']][i] %>% t()
      
      text = text %>% append(txt)
      label = label %>% append(lbl)
    }
    list(do.call(plyr::rbind.fill.matrix,text), do.call(plyr::rbind.fill.matrix,label))
  }
  
  train_ = data_prep(train)
  test_ = data_prep(test)
  
  # slice dataset
  tf_train = tensor_slices_dataset(list(train_[[1]],train_[[2]])) %>% 
    dataset_batch(batch_size = batch_size, drop_remainder = TRUE) %>% 
    dataset_shuffle(128) %>% dataset_repeat(epochs) %>% 
    dataset_prefetch(tf$data$experimental$AUTOTUNE)
  
  tf_test = tensor_slices_dataset(list(test_[[1]],test_[[2]])) %>% 
    dataset_batch(batch_size = batch_size)
  
  # create an input layer
  input = layer_input(shape=c(max_len), dtype='int32')
  hidden_mean = tf$reduce_mean(model_(input)[[1]], axis=1L) %>% 
    layer_dense(64,activation = 'relu')
  # create an output layer for binary classification
  output = hidden_mean %>% layer_dense(units=1, activation='sigmoid')
  model = keras_model(inputs=input, outputs = output)
  
  # compile with AUC score
  model %>% compile(optimizer= tf$keras$optimizers$Adam(learning_rate=3e-5, epsilon=1e-08, clipnorm=1.0),
                    loss = tf$losses$BinaryCrossentropy(from_logits=F),
                    metrics = tf$metrics$AUC())
  
  print(glue::glue('{ai_m[[i]][1]}'))
  # train the model
  history = model %>% keras::fit(tf_train, epochs=epochs, #steps_per_epoch=len/batch_size,
                validation_data=tf_test)
  gather_history[[i]]<- history
  names(gather_history)[i] = ai_m[[i]][1]
}
```

<center>
<a href="https://www.kaggle.com/henry090/transformers" class="colab-root">Reproduce in a<span class="colab-span">           Notebook</span></a>
</center>

<br>

Extract results to see the benchmarks:

``` r
res = sapply(1:3, function(x) {
  do.call(rbind,gather_history[[x]][["metrics"]]) %>% 
    as.data.frame() %>% 
    tibble::rownames_to_column() %>% 
    mutate(model_names = names(gather_history[x])) 
}, simplify = F) %>% do.call(plyr::rbind.fill,.) %>% 
  mutate(rowname = stringr::str_extract(rowname, 'loss|val_loss|auc|val_auc')) %>% 
  rename(epoch_1 = V1, epoch_2 = V2)
```


    Attaching package: 'dplyr'

    The following objects are masked from 'package:stats':

        filter, lag

    The following objects are masked from 'package:base':

        intersect, setdiff, setequal, union

<div class="datatables html-widget html-fill-item" id="htmlwidget-6197cfc87f0fba9f663f" style="width:100%;height:auto;"></div>
<script type="application/json" data-for="htmlwidget-6197cfc87f0fba9f663f">{"x":{"filter":"none","vertical":false,"data":[["1","2","3"],["val_auc","val_auc","val_auc"],[0.892,0.868,0.844],[0.893,0.855,0.845],["TFRobertaModel","TFGPT2Model","TFElectraModel"]],"container":"<table class=\"display\">
  <thead>
    <tr>
      <th> <\/th>
      <th>metric<\/th>
      <th>epoch_1<\/th>
      <th>epoch_2<\/th>
      <th>model_names<\/th>
    <\/tr>
  <\/thead>
<\/table>","options":{"dom":"t","columnDefs":[{"className":"dt-right","targets":[2,3]},{"orderable":false,"targets":0},{"name":" ","targets":0},{"name":"metric","targets":1},{"name":"epoch_1","targets":2},{"name":"epoch_2","targets":3},{"name":"model_names","targets":4}],"order":[],"autoWidth":false,"orderClasses":false}},"evals":[],"jsHooks":[]}</script>

Both the *RoBERTa* and *Electra* models show some additional improvements after 2 epochs of training, which cannot be said of *GPT-2*. In this case, it is clear that it can be enough to train a state-of-the-art model even for a single epoch.

## Conclusion

In this post, we showed how to use state-of-the-art NLP models from R.
To understand how to apply them to more complex tasks, it is highly recommended to review the [transformers tutorial](https://github.com/huggingface/transformers/tree/master/examples).

We encourage readers to try out these models and share their results below in the comments section!
