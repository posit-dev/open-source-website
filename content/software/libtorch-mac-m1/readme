# LibTorch builds for Apple Silicon

This repository contains a single GitHub Action workflow that can be used to trigger
LibTorch builds for the a specified branch.

Built libraries are uploaded to the [Releases page](https://github.com/mlverse/libtorch-mac-m1/releases)
and can be easily downloaded.

Build are using cmake instructions available [here](https://github.com/pytorch/pytorch/blob/master/docs/libtorch.rst),
with an extra `-DUSE_MPS=ON` CMake flag.

## System info

The build machine is:

- Mac mini M1 (2020)
- macOS Ventura 13.1
- Xcode (14.0.1)
- cmake version 3.22.1
- Built in a conda env with the following packages installed:

<details>
  <summary>Click me</summary>
  
```
# packages in environment at /Users/dfalbel/opt/miniconda3:
#
# Name                    Version                   Build  Channel
attrs                     22.1.0                   pypi_0    pypi
black                     22.3.0                   pypi_0    pypi
blas                      1.0                    openblas  
brotlipy                  0.7.0           py39h1a28f6b_1002  
bzip2                     1.0.8                h620ffc9_4  
c-ares                    1.18.1               h1a28f6b_0  
ca-certificates           2022.07.19           hca03da5_0  
certifi                   2022.9.14        py39hca03da5_0  
cffi                      1.15.1           py39h22df2f2_0  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
click                     8.1.3                    pypi_0    pypi
cmake                     3.22.1               hae769c0_0  
cmakelint                 1.4.1                    pypi_0    pypi
colorama                  0.4.5                    pypi_0    pypi
commonmark                0.9.1                    pypi_0    pypi
conda                     22.9.0           py39hca03da5_0  
conda-content-trust       0.1.1              pyhd3eb1b0_0  
conda-package-handling    1.8.1            py39h1a28f6b_0  
cryptography              37.0.1           py39h834c97f_0  
exceptiongroup            1.0.0rc9                 pypi_0    pypi
expat                     2.4.9                hc377ac9_0  
expecttest                0.1.3                    pypi_0    pypi
flake8                    3.8.2                    pypi_0    pypi
flake8-bugbear            20.1.4                   pypi_0    pypi
flake8-comprehensions     3.3.0                    pypi_0    pypi
flake8-executable         2.0.4                    pypi_0    pypi
flake8-pyi                20.5.0                   pypi_0    pypi
future                    0.18.2                   pypi_0    pypi
hypothesis                6.56.3                   pypi_0    pypi
idna                      3.3                pyhd3eb1b0_0  
junitparser               2.1.1                    pypi_0    pypi
krb5                      1.19.2               h3b8d789_0  
libcst                    0.4.7                    pypi_0    pypi
libcurl                   7.84.0               hc6d1d07_0  
libcxx                    12.0.0               hf6beb65_1  
libedit                   3.1.20210910         h1a28f6b_0  
libev                     4.33                 h1a28f6b_1  
libffi                    3.4.2                hc377ac9_2  
libgfortran               5.0.0           11_2_0_he6877d6_26  
libgfortran5              11.2.0              he6877d6_26  
libnghttp2                1.46.0               h95c9599_0  
libopenblas               0.3.20               hea475bc_0  
libssh2                   1.10.0               hf27765b_0  
libuv                     1.39.0               h1a28f6b_0  
lintrunner                0.9.3                    pypi_0    pypi
llvm-openmp               14.0.6               hc6e5704_0  
lz4-c                     1.9.3                hc377ac9_0  
mccabe                    0.6.1                    pypi_0    pypi
moreorless                0.4.0                    pypi_0    pypi
mpmath                    1.2.1                    pypi_0    pypi
mypy                      0.960                    pypi_0    pypi
mypy-extensions           0.4.3                    pypi_0    pypi
ncurses                   6.3                  h1a28f6b_2  
networkx                  3.0b1                    pypi_0    pypi
ninja                     1.10.2               hca03da5_5  
ninja-base                1.10.2               h525c30c_5  
numpy                     1.21.6                   pypi_0    pypi
openssl                   1.1.1q               h1a28f6b_0  
pathspec                  0.10.1                   pypi_0    pypi
pip                       21.2.4           py39hca03da5_0  
platformdirs              2.5.2                    pypi_0    pypi
pycodestyle               2.6.0                    pypi_0    pypi
pycosat                   0.6.3            py39h1a28f6b_0  
pycparser                 2.21               pyhd3eb1b0_0  
pyflakes                  2.2.0                    pypi_0    pypi
pygments                  2.13.0                   pypi_0    pypi
pyopenssl                 22.0.0             pyhd3eb1b0_0  
pysocks                   1.7.1            py39hca03da5_0  
python                    3.9.12               hbdb9e5c_0  
python.app                3                py39h1a28f6b_0  
pyyaml                    6.0              py39h1a28f6b_0  
readline                  8.1.2                h1a28f6b_1  
requests                  2.27.1             pyhd3eb1b0_0  
rhash                     1.4.1                hf27765b_1  
rich                      10.9.0                   pypi_0    pypi
ruamel-yaml               0.17.4                   pypi_0    pypi
ruamel-yaml-clib          0.2.6                    pypi_0    pypi
ruamel_yaml               0.15.100         py39h1a28f6b_0  
setuptools                63.4.1           py39hca03da5_0  
shellcheck-py             0.7.2.1                  pypi_0    pypi
six                       1.16.0             pyhd3eb1b0_1  
sortedcontainers          2.4.0                    pypi_0    pypi
sqlite                    3.38.3               h1058600_0  
stdlibs                   2022.10.9                pypi_0    pypi
sympy                     1.11.1                   pypi_0    pypi
tk                        8.6.11               hb8d0fd4_1  
toml                      0.10.2                   pypi_0    pypi
tomli                     2.0.1                    pypi_0    pypi
tomlkit                   0.11.5                   pypi_0    pypi
toolz                     0.11.2             pyhd3eb1b0_0  
torch                     1.14.0a0+git4155f5f           dev_0    <develop>
tqdm                      4.64.0           py39hca03da5_0  
trailrunner               1.2.1                    pypi_0    pypi
types-jinja2              2.11.9                   pypi_0    pypi
types-markupsafe          1.1.10                   pypi_0    pypi
types-pkg-resources       0.1.3                    pypi_0    pypi
types-protobuf            3.19.18                  pypi_0    pypi
types-pyyaml              6.0.7                    pypi_0    pypi
types-requests            2.27.25                  pypi_0    pypi
types-six                 1.16.15                  pypi_0    pypi
types-tabulate            0.8.8                    pypi_0    pypi
types-urllib3             1.26.25.1                pypi_0    pypi
typing-inspect            0.8.0                    pypi_0    pypi
typing_extensions         4.3.0            py39hca03da5_0  
tzdata                    2022a                hda174b7_0  
ufmt                      1.3.3                    pypi_0    pypi
urllib3                   1.26.9           py39hca03da5_0  
usort                     1.0.2                    pypi_0    pypi
wheel                     0.37.1             pyhd3eb1b0_0  
xz                        5.2.5                h1a28f6b_1  
yaml                      0.2.5                h1a28f6b_0  
zlib                      1.2.12               h5a0b063_2  
zstd                      1.5.2                h8574219_0
```

</details>
