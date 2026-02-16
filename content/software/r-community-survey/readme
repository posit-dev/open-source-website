# r-community-survey README
This repo contains the survey instruments, analysis documents, and data from the RStudio R Community Survey (formerly the R Learning Survey). This survey was initially created in fall 2018 and we have run it annually in December each year since. The 2020 survey is currently in the field.

This repo is organized simply:

- **2018/** contains the questions and data from the December 2018 survey
- **2019/** contains the questions and data from the December 2019 survey 
- **2020/** contains the questions from the December 2020 survey. It will be updated with the data after the survey has been fielded.

## Details of the surveys

### 2018

Below are some details about the 2018 survey and the methdology:

- The survey was fielded on the Internet between December 6 and December 31, 2018
- The survey was fielded in both English and Spanish versions
- Respondents were solicited from
	- community.rstudio.com
	- Twitter followers of RStudio employees and colleagues
	- reddit.com/datascience

We plan to keep the vast majority of the questions constant among years to allow us to see trends over time. However, I plan to 

**Bias warning**: Because we relied on the RStudio community to solicit respondents, this data probably has significant sampling bias. We can't really advertise it as representative of the broad R community; this sample is NOT random. However, even if it is just people who know us well enough to answer our survey, it is a large enough collection of data to be interesting nonetheless.

The information in this repository is organized as follows:

- **data/**: This directory holds the original survey responses and lightly coded versions of those responses, all in tab-delimited files. Separate files are used for English and Spanish versions of the survey.
- **dictionaries/**: This directory contains a collection of ad-hoc dictionaries for interpreting open-text responses (most of the survey results arrive as open text). No separate dictionaries are used for Spanish and English -- these are where we translate the Spanish responses into English ones when we do a composite analysis.
- **gendercoder/**: This package uses dictionaries to interpret the open text responses to gender identification, which can have a very large space of answers. Instead of inventing my own way of interpreting that data, I relied instead on more authoritative folks who have studied this problem. The gender identification used in the results shown are extremely simplistic; that was my choice for ease of presentation and should not reflect on the more sophisticated work in the actual package.
- **plots/**: This directory holds exploratory data plots that Carl Howe presented at rstudio::conf 2019.
- **slides/**: This directory holds a PDF of the slides presented at RStudio::conf 2019 along with some experimental attempts to create Xaringan R Markdown slides from the material. While I intended to do this initially, I only had a couple weeks between the closing of the survey and the conference, so I didn't complete the work there.

The R Markdown document for processing the survey is `process_survey.Rmd`. You may need to install a variety of packages to generate the plots shown. You will need to use `devtools` to install `gendercode` from `github`. You can Google for its location.

### 2019

The 2019 survey launched on December 13, 2019 and completed on January 10, 2020.

The survey in 2019 was largely the same as in 2018, but with the addition of a few more questions regarding Python, the discoverability of packages, and R Markdown. The processing script for 2019 remains incomplete (RStudio::conf 2020 and COVID-19 got in the way), but the directory structure follows the same format 2018. Not all dictionaries have been updated for 2019, so not every chunk of the processing script (process_survey.Rmd) will run. That said, the plots for the questions that I did analyze are in the **plots/** directory.

### 2020

The 2020 survey deleted several questions about the expected difficulty of learning R, while adding some additional questions about Python tools, Shiny applications, operating systems being used, and whether respondents feel as if they are part of the R community.

The 2020 survey will launch on December 10, 2020, and we expect it to complete on January 8, 2021.

You can take the survey at:

- English version: <https://rstd.io/r-survey-en>
- Spanish version: <https://rstd.io/r-survey-es>

You can view the survey questions as they are going to the field in the PDF files:

- 2020 English R Community Survey - Google Forms.pdf
- 2020 Spanish R Community Survey - Google Forms.pdf

Those question lists are in PDF format because Google Forms doesn't really have any easy way to download the contents of a form.

Carl Howe
RStudio, Inc.
carl@rstudio.com




