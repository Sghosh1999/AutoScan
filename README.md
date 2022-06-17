# Auto Scan [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

[<img src="https://www.innovagroupbcn.com/wp-content/uploads/2017/02/ocr.jpg" align="right" height="75" width="75">](https://streamlit.io)

> Text Extraction & NER Recognition Tool **using pytesseract**! Powered by **Python**!

## Live Demo :

### Table of Contents

- [Description](#description)
- [Usecase 1: Business Card Text Recognition](#usecase1)
  - [Features](#feat1)
- [Prerequisites](#prerq)
- [Installation Guide](#guide)

---

<a name="description"/>

## Description

This is an automatic Business Cards' Text Extraction & Labeling. BIO Tagging is used to prepare the training data and to train the Spacy NER Model.

|                               BIO Tagging                                |                             Grouped Labeling                             |
| :----------------------------------------------------------------------: | :----------------------------------------------------------------------: |
| ![](https://github.com/Sghosh1999/AutoScan/blob/main/images/mapping.JPG) | ![](https://github.com/Sghosh1999/AutoScan/blob/main/images/grouped.JPG) |

<a name="usecase1"/>

# Usecase 1 : Business cards Text Extraction & Labeling :heart_eyes:

It automatically detects the texts in the Input Business Cards and it tags the entities using BIO tagging.

|                                 Input Image                                  |                                BIO Tagging                                |
| :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| ![](https://github.com/Sghosh1999/AutoScan/blob/main/images/input_image.JPG) | ![](https://github.com/Sghosh1999/AutoScan/blob/main/images/bio_tags.JPG) |

<a name="feat1"/>

## Built With

This section should list any major frameworks that we have used to build the application.

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

---

<!-- GETTING STARTED -->

## Getting Started :robot:

In this section, A whole installation guide is mentioned. also trouble shooting guide is also given.

<a name="prerq"/>

## Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- Python ( Version 3.8.5)
- Git

<a name="guide"/>

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Sghosh1999/AutoScan.git
   ```

\*\*Open Command prompt and navigate to the folder(AutoGenerateTrackers)
`cd AutoScan`

2. Create a Virtual Python environment
   ```python
   python -m pip install virtualenv
   python -m virtualenv myendsv
   ```
3. Activate the Virtual environment
   ```python
   myenv\scripts\activate
   ```
4. Install necessary packages
   ```sh
   python -m pip install -r requirements.txt
   python -m pip install streamlit
   ```
5. Check if these two packages are installed or not: (optional)
   ```sh
   python -m streamlit --version
   ```
   If streamlit is not recognized, then run the command (optional)

```sh
  python -m pip install streamlit
```

Open the Prediction_testing_Single_Image file and run the code with the desired Business Card File.
