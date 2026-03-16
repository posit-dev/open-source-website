---
title: "BERT from R"
description: |
  A deep learning model - BERT from Google AI Research - has yielded state-of-the-art results in a wide variety of Natural Language Processing (NLP) tasks. In this tutorial, we will show how to load and train the BERT model from R, using Keras.
date: 2019-09-30
categories:
  - Natural Language Processing
  - TensorFlow/Keras
author:
  - name: Turgut Abdullayev
    url: https://github.com/henry090
    affiliation: AccessBank Azerbaijan
    affiliation_url: https://www.accessbank.az/en/
people:
  - Turgut Abdullayev
image: thumbnail.png
ported_from: ai
port_status: in-progress
---



*Today, we're happy to feature a guest post written by Turgut Abdullayev, showing how to use BERT from R. Turgut is a data scientist at AccessBank Azerbaijan. Currently, he is pursuing a Ph.D. in economics at Baku State University, Azerbaijan.*

[In the previous post, Sigrid Keydana](/blog/ai/2019-08-29-using-tf-from-r/) explained the logic behind the [reticulate package](https://rstudio.github.io/reticulate/) and how it enables interoperability between Python and R. So, this time we will build a classification model with [BERT](https://github.com/google-research/bert), taking into account one of the powerful capabilities of the reticulate package -- calling Python from R via importing Python modules.

Before we start, make sure that the Python version used is 3, as Python 2 can introduce lots of difficulties while working with BERT, such as Unicode issues related to the input text.

> Note: The R implementation presupposes TF Keras while by default, keras-bert does not use it. So, adding that environment variable makes it work.

``` r
Sys.setenv(TF_KERAS=1) 
# make sure we use python 3
reticulate::use_python('C:/Users/turgut.abdullayev/AppData/Local/Continuum/anaconda3/python.exe',
                       required=T)
# to see python version
reticulate::py_config()
```

``` r
python:         C:/Users/turgut.abdullayev/AppData/Local/Continuum/anaconda3/python.exe
libpython:      C:/Users/turgut.abdullayev/AppData/Local/Continuum/anaconda3/python37.dll
pythonhome:     C:\Users\TURGUT~1.ABD\AppData\Local\CONTIN~1\ANACON~1
version:        3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
Architecture:   64bit
numpy:          C:\Users\TURGUT~1.ABD\AppData\Local\CONTIN~1\ANACON~1\lib\site-packages\numpy
numpy_version:  1.16.4

NOTE: Python version was forced by use_python function
```

Luckily for us, a convenient way of importing BERT with Keras was created by Zhao HG. It is called [Keras-bert](https://github.com/CyberZHG/keras-bert). For us, this means that importing that same python library with `reticulate` will allow us to build a popular state-of-the-art model within R.

There are several methods to install keras-bert in Python.

- in Jupyter Notebook, run:

``` r
!pip install keras-bert
```

- in Terminal (Linux, Mac OS), run:

``` r
python3 -m pip install keras-bert
```

- in Anaconda prompt (Windows), run:

``` r
conda install keras-bert
```

After this procedure, you can check whether keras-bert is installed or not.

``` r
reticulate::py_module_available('keras_bert')
```

``` r
[1] TRUE
```

Finally, the TensorFlow version used should be 1.14/1.15. You can check it in the following form:

``` r
tensorflow::tf_version()
```

``` r
[1] ‘1.14’
```

In a nutshell:

``` r
pip install keras-bert
tensorflow::install_tensorflow(version = "1.15")
```

## What is BERT?

BERT[^1] is a pre-trained deep learning model introduced by Google AI Research which has been trained on Wikipedia and BooksCorpus. It has a unique way to understand the structure of a given text. Instead of reading the text from left to right or from right to left, BERT, using an attention mechanism which is called Transformer encoder[^2], reads the entire word sequences at once. So, it allows to understanding a word based on its surroundings. There are different kind of pre-trained BERT models but the main difference between them is trained parameters. In our case, [BERT](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip) with 12 encoder layers (Transformer Blocks), 768-hidden hidden units, 12-heads[^3], and 110M parameters will be used to create a text classification model.

## Model structure

Loading a pre-trained BERT model is straightforward. The [downloaded zip file](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip) contains:

- *bert_model.ckpt*, which is for loading the weights from the TensorFlow checkpoint
- *bert_config.json*, which is a configuration file
- *vocab.txt*, which is for text tokenization

``` r
pretrained_path = '/Users/turgutabdullayev/Downloads/uncased_L-12_H-768_A-12'
config_path = file.path(pretrained_path, 'bert_config.json')
checkpoint_path = file.path(pretrained_path, 'bert_model.ckpt')
vocab_path = file.path(pretrained_path, 'vocab.txt')
```

## Import Keras-Bert module via reticulate

Let's load keras-bert via `reticulate` and prepare a tokenizer object. The BERT tokenizer will help us to turn words into indices.

``` r
library(reticulate)
k_bert = import('keras_bert')
token_dict = k_bert$load_vocabulary(vocab_path)
tokenizer = k_bert$Tokenizer(token_dict)
```

### How does the tokenizer work?

BERT uses a WordPiece tokenization strategy. If a word is Out-of-vocabulary (OOV), then BERT will break it down into subwords. (eating =\> eat, ##ing).

<figure>
<img src="images/emb.png" width="549" alt="BERT input representation. The input embeddings are the sum of the token embeddings, the segmentation embeddings, and the position embeddings" />
<figcaption aria-hidden="true"><a href="https://arxiv.org/pdf/1810.04805.pdf">BERT input representation. The input embeddings are the sum of the token embeddings, the segmentation embeddings, and the position embeddings</a></figcaption>
</figure>

## Embedding Layers in BERT

There are 3 types of embedding layers in BERT:

- **Token Embeddings** help to transform words into vector representations. In our model dimension size is 768.
- **Segment Embeddings** help to understand the semantic similarity of different pieces of the text.
- **Position Embeddings** mean that identical words at different positions will not have the same output representation.

## Define model parameters and column names

As usual with keras, the batch size, number of epochs and the learning rate should be defined for training BERT.
Additionally, the *sequence length* is needed.

``` r
seq_length = 50L
bch_size = 70
epochs = 1
learning_rate = 1e-4

DATA_COLUMN = 'comment_text'
LABEL_COLUMN = 'target'
```

> Note: the max input length is 512, and the model is extremely compute intensive even on GPU.

## Load BERT model into R

We can load the BERT model and automatically pad sequences with `seq_len` function. Keras-bert[^4] makes the loading process very easy and comfortable.

``` r
model = k_bert$load_trained_model_from_checkpoint(
  config_path,
  checkpoint_path,
  training=T,
  trainable=T,
  seq_len=seq_length)
```

## Data structure, reading, preparation

The dataset for this post is taken from the [Kaggle Jigsaw Unintended Bias in Toxicity Classification competition](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification).

In order to prepare the dataset, we write a preprocessing function which will read and tokenize data simultaneously. Then, we feed the outputs of the function as input for BERT model.

``` r
# tokenize text
tokenize_fun = function(dataset) {
  c(indices, target, segments) %<-% list(list(),list(),list())
  for ( i in 1:nrow(dataset)) {
    c(indices_tok, segments_tok) %<-% tokenizer$encode(dataset[[DATA_COLUMN]][i], 
                                                       max_len=seq_length)
    indices = indices %>% append(list(as.matrix(indices_tok)))
    target = target %>% append(dataset[[LABEL_COLUMN]][i])
    segments = segments %>% append(list(as.matrix(segments_tok)))
  }
  return(list(indices,segments, target))
}
```

``` r
# read data
dt_data = function(dir, rows_to_read){
  data = data.table::fread(dir, nrows=rows_to_read)
  c(x_train, x_segment, y_train) %<-% tokenize_fun(data)
  return(list(x_train, x_segment, y_train))
}
```

## Load dataset

The way we have written the preprocess function, at first, it will read data, then add zeros and encode words into indices. Hence, we will have 3 output files:

- **x_train** is input matrix for BERT
- **x_segment** contains zeros for segment embeddings
- **y_train** is the output target which we should predict

``` r
c(x_train,x_segment, y_train) %<-% 
dt_data('~/Downloads/jigsaw-unintended-bias-in-toxicity-classification/train.csv',2000)
```

## Matrix format for Keras-Bert

The input data are in list format. They need to be extracted and transposed. Then, the train and segment matrices should be placed into the list.

``` r
train = do.call(cbind,x_train) %>% t()
segments = do.call(cbind,x_segment) %>% t()
targets = do.call(cbind,y_train) %>% t()

concat = c(list(train ),list(segments))
```

## Calculate decay and warmup steps

Using the Adam optimizer with warmup helps to lower the learning rate at the beginning of the training process. After certain training steps, the learning rate will gradually be increased, because learning new data without warmup can negatively affect a BERT model.

``` r
c(decay_steps, warmup_steps) %<-% k_bert$calc_train_steps(
  targets %>% length(),
  batch_size=bch_size,
  epochs=epochs
)
```

## Determine inputs and outputs, then concatenate them

In order to build a binary classification model, the output of the BERT model should contain 1 unit. Therefore, first of all, we should get input and output layers. Then, adding an additional dense layer to the output can perfectly meet our needs.

``` r
library(keras)

input_1 = get_layer(model,name = 'Input-Token')$input
input_2 = get_layer(model,name = 'Input-Segment')$input
inputs = list(input_1,input_2)

dense = get_layer(model,name = 'NSP-Dense')$output

outputs = dense %>% layer_dense(units=1L, activation='sigmoid',
                         kernel_initializer=initializer_truncated_normal(stddev = 0.02),
                         name = 'output')

model = keras_model(inputs = inputs,outputs = outputs)
```

This is how the model architecture looks like after adding a dense layer and padding input sequences.

``` r
Model
__________________________________________________________________________________________
Layer (type)                 Output Shape        Param #    Connected to                  
==========================================================================================
Input-Token (InputLayer)     (None, 50)          0                                        
__________________________________________________________________________________________
Input-Segment (InputLayer)   (None, 50)          0                                        
__________________________________________________________________________________________
Embedding-Token (TokenEmbedd [(None, 50, 768), ( 23440896   Input-Token[0][0]             
__________________________________________________________________________________________
Embedding-Segment (Embedding (None, 50, 768)     1536       Input-Segment[0][0]           
__________________________________________________________________________________________
Embedding-Token-Segment (Add (None, 50, 768)     0          Embedding-Token[0][0]         
                                                            Embedding-Segment[0][0]       
__________________________________________________________________________________________
Embedding-Position (Position (None, 50, 768)     38400      Embedding-Token-Segment[0][0] 
__________________________________________________________________________________________
Embedding-Dropout (Dropout)  (None, 50, 768)     0          Embedding-Position[0][0]      
__________________________________________________________________________________________
Embedding-Norm (LayerNormali (None, 50, 768)     1536       Embedding-Dropout[0][0]       
__________________________________________________________________________________________
Encoder-1-MultiHeadSelfAtten (None, 50, 768)     2362368    Embedding-Norm[0][0]          
__________________________________________________________________________________________
Encoder-1-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-1-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-1-MultiHeadSelfAtten (None, 50, 768)     0          Embedding-Norm[0][0]          
                                                            Encoder-1-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-1-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-1-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-1-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-1-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-1-FeedForward-Dropou (None, 50, 768)     0          Encoder-1-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-1-FeedForward-Add (A (None, 50, 768)     0          Encoder-1-MultiHeadSelfAttenti
                                                            Encoder-1-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-1-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-1-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-2-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-1-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-2-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-2-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-2-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-1-FeedForward-Norm[0][
                                                            Encoder-2-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-2-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-2-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-2-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-2-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-2-FeedForward-Dropou (None, 50, 768)     0          Encoder-2-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-2-FeedForward-Add (A (None, 50, 768)     0          Encoder-2-MultiHeadSelfAttenti
                                                            Encoder-2-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-2-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-2-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-3-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-2-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-3-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-3-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-3-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-2-FeedForward-Norm[0][
                                                            Encoder-3-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-3-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-3-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-3-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-3-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-3-FeedForward-Dropou (None, 50, 768)     0          Encoder-3-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-3-FeedForward-Add (A (None, 50, 768)     0          Encoder-3-MultiHeadSelfAttenti
                                                            Encoder-3-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-3-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-3-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-4-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-3-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-4-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-4-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-4-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-3-FeedForward-Norm[0][
                                                            Encoder-4-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-4-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-4-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-4-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-4-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-4-FeedForward-Dropou (None, 50, 768)     0          Encoder-4-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-4-FeedForward-Add (A (None, 50, 768)     0          Encoder-4-MultiHeadSelfAttenti
                                                            Encoder-4-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-4-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-4-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-5-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-4-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-5-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-5-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-5-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-4-FeedForward-Norm[0][
                                                            Encoder-5-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-5-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-5-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-5-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-5-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-5-FeedForward-Dropou (None, 50, 768)     0          Encoder-5-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-5-FeedForward-Add (A (None, 50, 768)     0          Encoder-5-MultiHeadSelfAttenti
                                                            Encoder-5-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-5-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-5-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-6-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-5-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-6-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-6-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-6-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-5-FeedForward-Norm[0][
                                                            Encoder-6-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-6-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-6-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-6-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-6-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-6-FeedForward-Dropou (None, 50, 768)     0          Encoder-6-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-6-FeedForward-Add (A (None, 50, 768)     0          Encoder-6-MultiHeadSelfAttenti
                                                            Encoder-6-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-6-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-6-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-7-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-6-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-7-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-7-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-7-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-6-FeedForward-Norm[0][
                                                            Encoder-7-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-7-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-7-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-7-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-7-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-7-FeedForward-Dropou (None, 50, 768)     0          Encoder-7-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-7-FeedForward-Add (A (None, 50, 768)     0          Encoder-7-MultiHeadSelfAttenti
                                                            Encoder-7-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-7-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-7-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-8-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-7-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-8-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-8-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-8-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-7-FeedForward-Norm[0][
                                                            Encoder-8-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-8-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-8-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-8-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-8-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-8-FeedForward-Dropou (None, 50, 768)     0          Encoder-8-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-8-FeedForward-Add (A (None, 50, 768)     0          Encoder-8-MultiHeadSelfAttenti
                                                            Encoder-8-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-8-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-8-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-9-MultiHeadSelfAtten (None, 50, 768)     2362368    Encoder-8-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-9-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-9-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-9-MultiHeadSelfAtten (None, 50, 768)     0          Encoder-8-FeedForward-Norm[0][
                                                            Encoder-9-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-9-MultiHeadSelfAtten (None, 50, 768)     1536       Encoder-9-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-9-FeedForward (FeedF (None, 50, 768)     4722432    Encoder-9-MultiHeadSelfAttenti
__________________________________________________________________________________________
Encoder-9-FeedForward-Dropou (None, 50, 768)     0          Encoder-9-FeedForward[0][0]   
__________________________________________________________________________________________
Encoder-9-FeedForward-Add (A (None, 50, 768)     0          Encoder-9-MultiHeadSelfAttenti
                                                            Encoder-9-FeedForward-Dropout[
__________________________________________________________________________________________
Encoder-9-FeedForward-Norm ( (None, 50, 768)     1536       Encoder-9-FeedForward-Add[0][0
__________________________________________________________________________________________
Encoder-10-MultiHeadSelfAtte (None, 50, 768)     2362368    Encoder-9-FeedForward-Norm[0][
__________________________________________________________________________________________
Encoder-10-MultiHeadSelfAtte (None, 50, 768)     0          Encoder-10-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-10-MultiHeadSelfAtte (None, 50, 768)     0          Encoder-9-FeedForward-Norm[0][
                                                            Encoder-10-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-10-MultiHeadSelfAtte (None, 50, 768)     1536       Encoder-10-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-10-FeedForward (Feed (None, 50, 768)     4722432    Encoder-10-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-10-FeedForward-Dropo (None, 50, 768)     0          Encoder-10-FeedForward[0][0]  
__________________________________________________________________________________________
Encoder-10-FeedForward-Add ( (None, 50, 768)     0          Encoder-10-MultiHeadSelfAttent
                                                            Encoder-10-FeedForward-Dropout
__________________________________________________________________________________________
Encoder-10-FeedForward-Norm  (None, 50, 768)     1536       Encoder-10-FeedForward-Add[0][
__________________________________________________________________________________________
Encoder-11-MultiHeadSelfAtte (None, 50, 768)     2362368    Encoder-10-FeedForward-Norm[0]
__________________________________________________________________________________________
Encoder-11-MultiHeadSelfAtte (None, 50, 768)     0          Encoder-11-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-11-MultiHeadSelfAtte (None, 50, 768)     0          Encoder-10-FeedForward-Norm[0]
                                                            Encoder-11-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-11-MultiHeadSelfAtte (None, 50, 768)     1536       Encoder-11-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-11-FeedForward (Feed (None, 50, 768)     4722432    Encoder-11-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-11-FeedForward-Dropo (None, 50, 768)     0          Encoder-11-FeedForward[0][0]  
__________________________________________________________________________________________
Encoder-11-FeedForward-Add ( (None, 50, 768)     0          Encoder-11-MultiHeadSelfAttent
                                                            Encoder-11-FeedForward-Dropout
__________________________________________________________________________________________
Encoder-11-FeedForward-Norm  (None, 50, 768)     1536       Encoder-11-FeedForward-Add[0][
__________________________________________________________________________________________
Encoder-12-MultiHeadSelfAtte (None, 50, 768)     2362368    Encoder-11-FeedForward-Norm[0]
__________________________________________________________________________________________
Encoder-12-MultiHeadSelfAtte (None, 50, 768)     0          Encoder-12-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-12-MultiHeadSelfAtte (None, 50, 768)     0          Encoder-11-FeedForward-Norm[0]
                                                            Encoder-12-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-12-MultiHeadSelfAtte (None, 50, 768)     1536       Encoder-12-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-12-FeedForward (Feed (None, 50, 768)     4722432    Encoder-12-MultiHeadSelfAttent
__________________________________________________________________________________________
Encoder-12-FeedForward-Dropo (None, 50, 768)     0          Encoder-12-FeedForward[0][0]  
__________________________________________________________________________________________
Encoder-12-FeedForward-Add ( (None, 50, 768)     0          Encoder-12-MultiHeadSelfAttent
                                                            Encoder-12-FeedForward-Dropout
__________________________________________________________________________________________
Encoder-12-FeedForward-Norm  (None, 50, 768)     1536       Encoder-12-FeedForward-Add[0][
__________________________________________________________________________________________
Extract (Extract)            (None, 768)         0          Encoder-12-FeedForward-Norm[0]
__________________________________________________________________________________________
NSP-Dense (Dense)            (None, 768)         590592     Extract[0][0]                 
__________________________________________________________________________________________
output (Dense)               (None, 1)           769        NSP-Dense[0][0]               
==========================================================================================
Total params: 109,128,193
Trainable params: 109,128,193
Non-trainable params: 0
__________________________________________________________________________________________
```

## Compile model and begin training

Aus usual with Keras, before training a model, we need to compile the model. And using `fit()`, we feed it the R arrays.

``` r
model %>% compile(
  k_bert$AdamWarmup(decay_steps=decay_steps, 
                    warmup_steps=warmup_steps, lr=learning_rate),
  loss = 'binary_crossentropy',
  metrics = 'accuracy'
)

model %>% fit(
  concat,
  targets,
  epochs=epochs,
  batch_size=bch_size, validation_split=0.2)
```

## Conclusion

In this post, we've shown how we can use Keras to conveniently load, configure, and train a BERT model.

[^1]: [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)

[^2]: [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)

[^3]: Attention --- focuses on salient parts of input by taking a weighted average of them. 768 hidden units divided by 12 chunks and each chunk will have 64 output dimensions, afterward, the result from each chunk will be concatenated and forwarded to the next layer

[^4]: [Implementation of the BERT. Official pre-trained models could be loaded for feature extraction and prediction](https://github.com/CyberZHG/keras-bert)
