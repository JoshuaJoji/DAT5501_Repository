import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('UK_Pop_1950_2025.csv')
df.columns = ['Year', 'Population']
df['Year'] = pd.to_numeric(df['Year'])
df['Population'] = pd.to_numeric(df['Population'])

train = df.iloc[:-10]
test = df.iloc[-10:]

x_train = train['Year'].values
y_train = train['Population'].values
x_test = test['Year'].values
y_test = test['Population'].values

#Uncertainties as 2.5% of the population values
sigma = 0.025 * df['Population'].values

selected_orders = [3, 5, 9] #Polynomial orders to compare

plt.figure(figsize=(10,6))

plt.errorbar(df['Year'], df['Population'], yerr=sigma, fmt='o', color='tab:blue',
             ecolor='lightblue', elinewidth=1, capsize=2, label='Observed data with uncertainties')

colors = ['green', 'orange', 'red']
for i, deg in enumerate(selected_orders):
    coeffs = np.polyfit(x_train, y_train, deg)
    poly = np.poly1d(coeffs)
    x_fit = np.linspace(df['Year'].min(), df['Year'].max(), 500)
    y_fit = poly(x_fit)
    
    style = '-' if i == 0 else '--' if i == 1 else ':'
    
    if deg == 5:
        label_text = f'Polynomial order {deg} (Best Fit)'
    elif deg == 3:
        label_text = f'Polynomial order {deg} (Underfitting)'
    elif deg == 9:
        label_text = f'Polynomial order {deg} (Overfitting)'
    else:
        label_text = f'Polynomial order {deg}'

    plt.plot(x_fit, y_fit, style, color=colors[i],
         linewidth=2, label=label_text)

fit_limit = x_train.max()  #last year of training data
plt.axvline(x=fit_limit, color='black', linestyle='--', label=f'Fit limit ({int(fit_limit)})')

plt.title('UK Population Forecast – Weighted Polynomial Fits Comparison', fontsize=13)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()