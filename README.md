# DAT5501 Repository

This repository contains all Python scripts, datasets, and coursework exercises completed as part of the DAT5501 Analysis, Software and Career Practice module.
The work is organised into folders, each containing a specific activity, mini-project, or practical task.

---

## Folder Structure & Summaries

- **22_09_25**
Contains introductory Python script:
- print ("Hello, World!").py – Basic test script printing “Hello, World!”.

- **25_09_25**
Foundational Python programming tasks:
- add_number.py – Simple script for adding numbers.
- functions.py – Contains example functions demonstrating Python function definitions.
- functions_testing.py – Test file used to verify the behaviour of functions.py.

- **06_10_25**
Date and calendar practice:
- calendar_printer.py – Script for printing a formatted calendar for a given month & year.

- **20_10_25**
Time, date, and data-handling tasks:
- asset_price.py – Asset price modelling exercise.
- date_diff_test.py – Tests for calculating date differences.
- duration_calculator.py – Script for computing durations between dates.
- random_dates.csv – Dataset used by the above scripts.

- **23_10_25**
Pandas and data wrangling with US election data:
- pandas_US_election.py – Data analysis using pandas on US primary election data.
- test_pandas_US_election.py – Unit tests for the election analysis script.
- US-2016-primary.csv – Dataset used in the analysis.

- **10_11_25**
Sorting and analysing financial data:
- asset_price_sorting.py – Sorting and evaluating asset price movements.
- amazon_historical_nasdaq.csv – Historical Amazon stock dataset used in script.

- **13_11_25_17_11_25**
Polynomial fitting, forecasting & model-selection activities:
- fitting_forecast_bic.py – Weighted polynomial forecasting with BIC model selection and parameter uncertainty.
- fitting_forecas_model_selection.py – Comparison of polynomial orders and forecasting behaviour.
- Fitting_Forecasting_Activity.py – χ² (chi-squared) calculations and BIC evaluation.
- fitting_forecasting_chi.py – Detailed chi-squared and BIC model analysis.
- UK_Pop_1950_2025.csv – UK population dataset used for forecasting.

- **24_11_25_27_11_25**
Supervised machine learning:
- mushroom_decision_tree.py – Decision Tree classifier on the Agaricus-Lepiota mushroom dataset (edible vs poisonous).
Includes data encoding, train/test split, model fitting, accuracy score, and tree visualisation.

- **OWiD_Presentation**
Work related to an Our World in Data–based presentation:
- gdp_vs_meat_consumption.py – Analysis of GDP vs global meat-consumption patterns.
- meat-consumption-vs-gdp-per-capita.csv – Dataset used for the analysis.

- **Personal_Projects**
Independent projects:
- predict_prem_league.py – Prediction modelling for Premier League football results.
- table_tennis_game.py – Simple interactive table-tennis scoring game.
- internet_speed_tracker/ – Sub-folder containing a Python project to log and track internet speed over time.
- E0.csv – Dataset used in one of the personal scripts.

---

## Requirements

- Python 3.13  
- Libraries:
  - `pandas>=2.0.0`
  - `matplotlib>=3.8.0`
  - `numpy>=1.26.0`
  - `scikit-learn>=1.5.0`

Install dependencies:
```bash
pip install -r requirements.txt
```
---

## How to Run
Clone the repository:
```bash
git clone https://github.com/JoshuaJoji/DAT5501_Repository.git
cd DAT5501_Repository
```
Navigate to folder and run script

---

## Key Achievements
- Implemented a **decision tree classifier** on the Mushroom dataset.
- Used **unit testing** to validate functionality across weekly tasks.
- Analysed Nasdaq financial data and measured sorting complexity vs n log n.
- Created **personal mini projects** including a Premier League predictor and internet speed tracker.
- Performed **polynomial fitting and forecasting** with statistical model selection (χ², BIC).