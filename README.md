# MRes Project - Whale detection in Remote Sensing Imagery using Deep Learning

 [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
 <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Description

This repository contains the work for an MRes for the AI4ER CDT investigating the automated detection of whales in remote sensing data. It includes code to preprocess aerial and satellite imagery for use with YOLOv5 models. Model weights and instructions are included to test the performance of these models for counting gray whales in satellite imagery. 

## Getting started

Clone the repository:

```
git clone https://github.com/KMacfarlaneGreen/mres_whales.git
```
Navigate to the directory and install the conda environment:

```
cd mres_whales
```

## Requirements
- Python 3.8+
- See requirements directory for the full list of dependencies

Requirements can be installed:
```
pip install -r requirements/requirements.txt
```


## Project Organization
```
├── LICENSE
├── Makefile           <- Makefile with commands like `make init` or `make lint-requirements`
├── README.md          <- The top-level README for developers using this project.
|
├── notebooks          <- Jupyter notebooks
│   ├── exploratory    <- Notebooks for initial exploration.
│   └── reports        <- Notebooks demonstrating preprocessing regimes.
|
├── requirements       <- Directory containing the requirement files.
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── preprocessing  <- Scripts to turn raw aerial and satellite data into clean data and features for modeling
|   |
│   ├── models         <- Instructions to train models and then use trained models to make
│   │                     predictions
│   │
│   └── tests          <- Scripts for unit tests of your functions
│
└── setup.cfg          <- setup configuration file for linting rules
```

---

Project template created by the [Cambridge AI4ER Cookiecutter](https://github.com/ai4er-cdt/ai4er-cookiecutter).