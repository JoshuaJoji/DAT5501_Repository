# DAT5501 Repository

This repository contains all Python scripts, datasets, and coursework exercises completed as part of the DAT5501 Analysis, Software and Career Practice module.
The work is organised into folders, each containing a specific activity, mini-project, or practical task.

---

## Folder Structure & Summaries

- **22_09_25**  
  Contains introductory Python script:
  - `print("Hello, World!").py` – Basic test script printing “Hello, World!”.

- **25_09_25**  
  Foundational Python programming tasks:
  - `add_number.py` – Simple script for adding numbers.
  - `functions.py` – Example Python functions.
  - `functions_testing.py` – Tests for `functions.py`.

- **06_10_25**  
  Date and calendar practice:
  - `calendar_printer.py` – Prints a monthly calendar.

- **20_10_25**  
  Time, date, and data-handling tasks:
  - `asset_price.py` – Asset price modelling.
  - `date_diff_test.py` – Tests for date difference calculations.
  - `duration_calculator.py` – Computes duration between dates.
  - `random_dates.csv` – Dataset used in these scripts.

- **23_10_25**  
  Pandas and data wrangling:
  - `pandas_US_election.py` - analysis of US 2016 primary data.
  - `test_pandas_US_election.py` - unit tests for verifying functions.
  - `US-2016-primary.csv` - dataset used for the tasks.

- **10_11_25**  
  Sorting and financial analysis:
  - `asset_price_sorting.py` - measures sorting performance of price changes.
  - `amazon_historical_nasdaq.csv` - dataset for sorting experiments.

- **13_11_25_17_11_25**  
  Polynomial fitting, forecasting & model selection:
  - `fitting_forecast_bic.py` - model selection using BIC.
  - `fitting_forecas_model_selection.py` - comparison of polynomial fits.
  - `Fitting_Forecasting_Activity.py` - χ²/dof analysis for polynomial models.
  - `fitting_forecasting_chi.py` - full χ² and BIC workflow with diagnostics.
  - `UK_Pop_1950_2025.csv` - dataset used for population forecasting.

- **24_11_25_27_11_25**  
  Machine learning (Decision Tree):
  - `mushroom_decision_tree.py` - trains and plots a Decision Tree classifier for mushroom edibility.

- **OWiD_Presentation**
  - `gdp_vs_meat_consumption.py` - examines GDP vs meat consumption.
  - `meat-consumption-vs-gdp-per-capita.csv` - supporting dataset.

- **Personal_Projects**
  - `predict_prem_league.py` - simple premier league outcome prediction.
  - `table_tennis_game.py` - small interactive game.
  - `internet_speed_tracker/` - logs and analyses internet speeds over time.
  - `E0.csv` - dataset linked to a personal script.

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

---