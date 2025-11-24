**This Activity is for Model Validation and Testing**

Population data of UK (1950-2025) is extracted from "https://www.macrotrends.net/global-metrics/countries/gbr/united-kingdom/population"

Training was done on data up to 2015, and the later years were used for comparison.

Scripts analysed:
1. fitting_forecast_model_selection.py
2. Fitting_Forecasting_Activity.py
3. fitting_forecasting_chi.py
4. fitting_forecast_bic.py

Results:

1. fitting_forecast_model_selection.py (13_11_25)
Degree 3: Underfitting
Degree 5: Best Fit
Degree 9: Overfitting
Plot includes measurement uncertainties (2.5%)

2. Fitting_Forecasting_Activity.py (13_11_25)
Fits for polynomial models from 1-9
Best BIC Polynomial Fit: Order 5. This provides the best compromise bwetween fit and complexity.

3. fitting_forecasting_chi.py (13_11_25)
Refitting model 5 with the full covariance information. 

4. fitting_forecast_bic.py (17_11_25 + 20_11_25)
Parameter estimates with uncertainties:
a0 = -1.4248e-01 ± 1.3909e-05
a1 = 1.4139e+03 ± 6.2385e-02
a2 = -5.6118e+06 ± nan
a3 = 1.1136e+10 ± 2.9081e+05
a4 = -1.1049e+13 ± 9.2010e+08
a5 = 4.3845e+15 ± 5.8404e+11

The parameters define the polynomial curve, and their ± uncertainties show how certain the model is about each one; the NaN appears because a high-degree polynomial produces correlated, unstable coefficients, which is common and expected.