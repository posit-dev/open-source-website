# rscrypt

[![Build Status](https://travis-ci.org/rstudio/rscrypt.png?branch=master)](https://travis-ci.org/rstudio/rscrypt)

rscrypt is an R package for a collection of scrypt cryptographic functions. Scrypt is a
password-based key derivation function created by Colin Percival. The algorithm was specifically
designed to make it costly to perform large-scale custom hardware attacks by requiring large
amounts of memory.

## Requirements

This package makes use of native code, you will need to have a R package development 
environment installed on your system:

__Windows:__ RTools for building packages
__Mac OSX:__ XCode Command Line Tools for building packages

## Installation

To install directly from GitHub, run this:

```
if (!require("devtools"))
    install.packages("devtools")
devtools::install_github("rstudio/rscrypt")
```

## Usage

Hash a password:
```
hashed <- scrypt::hashPassword("good password")
```

Verify a hashed password:
```
scrypt::verifyPassword(hashed, "bad bassword")
[1] FALSE

scrypt::verifyPassword(hashed, "good password")
[1] TRUE
```

Key derivation function
```
password <- charToRaw("my password")
salt <- sample(1:10, 32, replace=TRUE)
scrypt::scrypt(password, salt, 65536, 8, 1)
```

## Password Hashing

The `hashPassword` and `verifyPassword` functions are designed be compatible with the
node.js scrypt package. The output from `hashPassword` is a base64 encoded string
containing multiple pieces of information that are required to verify the hash later on.
Included in this output are the n, r and p parameters for the scrypt function, as well as
a checksum and HMAC for verifying the integrity of the hash. Below is the format the hash.


### Hash Format
```
offset	length
0	6	"scrypt"
6	1	scrypt data file version number (0)
7	1	log2(n) (big-endian must be between 1 and 63 inclusive)
8	4	r (big-endian integer; must satisfy r * p < 2^30)
12	4	p (big-endian integer; must satisfy r * p < 2^30)
16	32	salt
48	16	first 16 bytes of SHA256(bytes 0 .. 47)
64	32	HMAC-SHA256(bytes 0 .. 63)
```

