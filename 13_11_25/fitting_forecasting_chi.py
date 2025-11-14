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

plt.figure(figsize=(10,6))
plt.scatter(df['Year'], df['Population'], color='black', label='Actual data')

for deg in range(1, 10):
    coeffs = np.polyfit(x_train, y_train, deg)
    poly = np.poly1d(coeffs)
    x_future = np.arange(x_train.min(), x_train.max() + 11)
    y_future = poly(x_future)
    plt.plot(x_future, y_future, label=f'Order {deg}')

plt.title('Polynomial Fits for UK Population (1950–2025)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()

# --------------------------------
# --- Finding Chi-squared stat ---
# --------------------------------

x = df['Year'].values
y = df['Population'].values
N = len(x)

sigma = 0.01 * y

chi2_values = []
degrees = range(1, 10)

for deg in degrees:
    coeffs = np.polyfit(x, y, deg)
    poly = np.poly1d(coeffs)
    y_pred = poly(x)

    chi2 = np.sum(((y - y_pred) ** 2) / (sigma ** 2))
    dof = N - (deg + 1)
    chi2_per_dof = chi2 / dof
    chi2_values.append(chi2_per_dof)

    print(f"Degree {deg}: χ²/ν = {chi2_per_dof:.4f}")

plt.figure(figsize=(8,5))
plt.plot(degrees, chi2_values, 'o-', color='purple')
plt.title('χ² per Degree of Freedom for Polynomial Fits')
plt.xlabel('Polynomial Order')
plt.ylabel('χ²/ν')
plt.grid(True)
plt.show()

sorted_results = sorted(zip(degrees, chi2_values), key=lambda x: x[1])
best_three = sorted_results[:3]

print("Best fits (lowest χ² per degree of freedom):") #display best three
for rank, (deg, val) in enumerate(best_three, start=1):
    print(f"{rank}. Order {deg} χ²/ν = {val:.4f}")