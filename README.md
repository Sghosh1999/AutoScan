# Daily Tracker ++ [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

[<img src="https://media.istockphoto.com/vectors/unique-modern-creative-elegant-letter-d-based-vector-icon-logo-vector-id1125625274?k=6&m=1125625274&s=612x612&w=0&h=U-fRNFEEezcFQ5M8EPjiqUTiqvhHt3lUN2s9CbaVX94=" align="right" height="75" width="75">](https://streamlit.io)

> The fastest way to build **Daily, Weekly & Monthly Trackers**! Powered by **Python**!

## Live Demo : https://tracker-generate.herokuapp.com/

### Table of Contents

- [Description](#description)
- [Usecase 1: Daily tracker Generation](#usecase1)
  - [Features](#feat1)
  - [Application Demo](#demo1)
- [Usecase 2: Weekly & Monthly Generation](#usecase2)
  - [Features](#feat2)
  - [Application Demo](#demo2)
- [Prerequisites](#prerq)
- [Installation Guide](#guide)

---

<a name="description"/>

## Description

This is a automatic Tracker generation Web Application which can generate daily, weekly and monthly trackers. It has been enhanced to generate group level trackers also.

|                                   Multiuser Weekly & Monthly Trcaker Generator                                    |                                              Daily Tracker Generator                                              |
| :---------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/Sghosh1999/AutoGenerateTrackers/blob/da2d8f24090a6ec12cfe3a8b715704887987eae8/demos/a.jpg) | ![](https://github.com/Sghosh1999/AutoGenerateTrackers/blob/da2d8f24090a6ec12cfe3a8b715704887987eae8/demos/b.jpg) |

<a name="usecase1"/>

# Usecase 1 : Daily Trcaker Generation :heart_eyes:

In this use case, user can generate his daily tracker for a **single day as well as multiple days** (_In case he/she forgot to fill daily_).

<a name="feat1"/>

## Features

- Automatic Generates **_Daily Trackers_** based on Date and corrosponding Tasks.
- If a user is not filling his daily tracker for consecutive two days , **an email notification will be sent** to the given email-address.
- User need to give **Start date and end date** in order o fill up the tasks.

<a name="demo1"/>

### Application Demo

<p align="center">
  <img src="https://github.com/Sghosh1999/AutoGenerateTrackers/blob/49d6ce9efecaf581b7227c97dc5d3c6f3d24ef75/demos/daily_trcaker_demo.gif" alt="animated" />
</p>

<a name="usecase2"/>

# Usecase 2 : Weekly & Monthly Generation :heart_eyes:

In this use case, user can generate his **weekly as well as monthly tracker** by giving his daily tracker as Input. Not only that, if a users want to generate **group weekly trackers and group monthly trackers** he can also do that by giving the users daily trackers.

<a name="feat2"/>

## Features

- Automatic Generates **_Weekly Trackers_** and **_Monthly Trackers_** based on Daily Trackers.
- Text preprocessing is handled. Automatic **new line** and **Number formatting** is being taken care of.
- Unnecessary phrases **( Holiday, Leave) is excluded**.
- **Text Wrapping of the csv** file is handled. **Proper Orientation** is handled.
- **Null value exception** is handled.
- It supports both **single user** and **multi user** purposes.
- Ex ( Group weekly Trackers):

| Name     | Week 1               | Week 2    | ... | Week n    |
| -------- | -------------------- | --------- | --- | --------- |
| Person 1 | 1. Completed Task A. | 1. Task C | ... | 1. Task D |
| Person 2 | 1. Completed Task B  | 1. Task E | ... | 1. Task F |
| ...      | ...                  | ...       | ... | ...       |
| Person n | 1. Completed Task n  | 1. Task n | ... | 1. Task n |

---

<!--
### Application Dem
| Single User |Multiple User |
|--|--|
|<img src="https://github.com/Sghosh1999/AutoGenerateTrackers/blob/78abe5fbcf58ed1054bbfc28e3b3029ba6835384/demos/week_month_demo1.gif" alt="animated" />|<img src="https://github.com/Sghosh1999/AutoGenerateTrackers/blob/ad55ed7d7e4aecf078b2c512f85cff2494479392/demos/multi_user_demo.gif" alt="animated" />|
 -->

<a name="demo2"/>

### Application Demo (Single User)

<p align="center">
  <img src="https://github.com/Sghosh1999/AutoGenerateTrackers/blob/78abe5fbcf58ed1054bbfc28e3b3029ba6835384/demos/week_month_demo1.gif" alt="animated" />
</p>

### Application Demo (Multiple User)

<p align="center">
  <img src="https://github.com/Sghosh1999/AutoGenerateTrackers/blob/ad55ed7d7e4aecf078b2c512f85cff2494479392/demos/multi_user_demo.gif" alt="animated" />
</p>

---

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
   git clone https://github.com/Sghosh1999/AutoGenerateTrackers.git
   ```

\*\*Open Command prompt and navigate to the folder(AutoGenerateTrackers)
` cd AutoGenerateTrackers `

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
   python -m pip install openpyxl
   ```
5. Check if these two packages are installed or not: (optional)
   ```sh
   python -m streamlit --version
   ```
   If streamlit is not recognized, then run the command (optional)

```sh
  python -m pip install streamlit
```

## Running the Application

```python
python -m streamlit run app.py
```

- For the first time it will ask you for the email. Please provide the email and the application will be open in your browser.

## Demo Tracker files for Testing 🕶️

- In the **_demo_trackers folder_** go to **_multi_user_trackers_**. In the **_input_files_** there are 2 sample daily trackers. You can use it to test the group weekly and monthly Trackers
- In the **_output_files_** the output files are present.

### Built with :heart: by Team 8 ( Droid )
