# Project_1_Team_1

## Z-Score Calculator App using CSV Data pulled from "” Capital IQ
**Objective:** The goal of this project is to build a Z-Score calculator to automate the process of calculating Z-Scores, and to be able to calculate Z-Scores for many companies in a short amount of time. We are calculating the Altman z-score of a few utility companies traded in the stock market .
In order to calculate the z-score we need to know the company's finances. A score close to zero suggests that the company might be heading for bankruptcy, while a score closer to 3 is less likely to default on its loans. The goal of building this app is to find out which companies are doing well financially, but whose shares are trading below its intrinsic value or has a lower PE ratio compared to its peers in the same sector. 


----

## Directory
[Program](main.py)
[Filtering/Functions] (utilities)
[Data] (Resources, z_score_calculator)

----

## *Technologies*
This feature/project leverages Python 3.7 with the following packages:
* [questionary] (https://github.com/tmbo/questionary) - for interactive user prompts and dialogs
* [sys] (https://github.com/python/cpython/blob/main/Python/sysmodule.c) - For exiting the app if user credentials fail to meet criteria
* [pandas] (https://github.com/pandas-dev/pandas) - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures
* [Path] (https://github.com/nemec/pathlib) - Path manipulation library for .Net

---

## Installation Guide
Before running the application first install the following dependencies.
‘’'python
    pip installl pandas
    pip install questionary
    pip install sys
    
---

## *Usage*
Step1: We first define the function load_stock_data() and we will pass the csvpath variable through it.
The csv path will be provided by the user.
Step2: If path does not exist, app will print error message and exit
Step3: If the path exist, the app will prompt user to select one of the stocks displayed on screen and then to hit enter
The app will read the csv file into a data frame using pandas.
Step4: The app also replaces the strings”NYSE:” and “NasdaqGS” with ” ” (blank space) for legibility reasons.
Step5: After the user selects the stock they want analyzed, the app call on the calculator to perform the function and displays the zscore of previous quarters
Step6: We have taken a sample of one stock to plot a bar chart

---

## *Contributors*
Brought to you by Kali, Michael, Simon
