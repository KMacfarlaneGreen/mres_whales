# Source code folder

This folder contains scripts and instructions for the analysis performed in the project. Scripts for processing satellite and aerial imagery are in the 'preprocessing' folder. The weights from the trained 'YOLOv5' implementations are stored in 'models/weights'.

The source folder is structured as follows:
```
src
├── __init__.py    <- Makes src a Python module
|
├── preprocessing  <- Scripts to turn raw data into clean data and features for modeling
│
├── models         <- Instructions to train models and use trained models to make
│                     predictions
└── tests          <- Scripts for unit tests of  functions
```
