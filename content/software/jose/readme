# jose

[![Build Status](https://app.travis-ci.com/jeroen/jose.svg?branch=master)](https://app.travis-ci.com/jeroen/jose)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/jeroen/jose?branch=master&svg=true)](https://ci.appveyor.com/project/jeroen/jose)
[![Coverage Status](https://codecov.io/github/jeroen/jose/coverage.svg?branch=master)](https://app.codecov.io/github/jeroen/jose?branch=master)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/jose)](http://cran.r-project.org/package=jose)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/jose)](http://cran.r-project.org/web/packages/jose/index.html)

> JavaScript Object Signing and Encryption

Read and write JSON Web Keys (JWK, rfc7517), generate and verify JSON
Web Signatures (JWS, rfc7515) and encode/decode JSON Web Tokens (JWT, rfc7519).
These standards provide modern signing and encryption formats that are natively
supported by browsers via the JavaScript WebCryptoAPI, and used by services 
like OAuth 2.0, LetsEncrypt, and Github Apps.

## Documentation

Vignettes for the R package:

 - [Reading/Writing JSON Web Keys (JWK) in R](https://cran.r-project.org/web/packages/jose/vignettes/jwk.html)
 - [Encoding/Decoding JSON Web Tokens (JWT) in R](https://cran.r-project.org/web/packages/jose/vignettes/jwt.html)

Specifications and standards:

 - JOSE RFC Tracker: https://datatracker.ietf.org/wg/jose/documents/
 - Browser WebCryptoAPI API: https://www.w3.org/TR/WebCryptoAPI/#jose
 - ACME Protocol (LetsEncrypt): https://ietf-wg-acme.github.io/acme/draft-ietf-acme-acme.html

## JSON Web Keys (JWK)

```r
library(jose)

# generate an ecdsa key
key <- ec_keygen("P-521")
write_jwk(key)
write_jwk(as.list(key)$pubkey)

# Same for RSA
key <- rsa_keygen()
write_jwk(key)
write_jwk(as.list(key)$pubkey)
```

## JSON Web Tokens (JWT)

```r
# HMAC signing
mysecret <- "This is super secret"
token <- jwt_claim(name = "jeroen", session = 123456)
sig <- jwt_encode_hmac(token, mysecret)
jwt_decode_hmac(sig, mysecret)

# RSA encoding
mykey <- openssl::rsa_keygen()
pubkey <- as.list(mykey)$pubkey
sig <- jwt_encode_sig(token, mykey)
jwt_decode_sig(sig, pubkey)

# Same with EC
mykey <- openssl::ec_keygen()
pubkey <- as.list(mykey)$pubkey
sig <- jwt_encode_sig(token, mykey)
jwt_decode_sig(sig, pubkey)
```
