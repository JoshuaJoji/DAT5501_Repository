import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Load dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "UK_Pop_1950_2025.csv")
df = pd.read_csv(csv_path)
#print(df.head(10))
df.columns = ['Year', 'Population']
df['Year'] = pd.to_numeric(df['Year'])
df['Population'] = pd.to_numeric(df['Population'])

#Split data into training and testing sets
train = df.iloc[:-10]
test = df.iloc[-10:]
#print(test)

# Prepare training and testing data
x_train = train['Year'].values
y_train = train['Population'].values

# Prepare testing data
x_test = test['Year'].values
y_test = test['Population'].values

#Plot actual data
plt.figure(figsize=(10,6))
plt.scatter(df['Year'], df['Population'], color='black', label='Actual data')

#Fit and plot polynomials of degree 1 to 9
for deg in range(1, 10):
    coeffs = np.polyfit(x_train, y_train, deg)
    poly = np.poly1d(coeffs)

    x_future = np.arange(x_train.min(), x_train.max() + 11)
    y_future = poly(x_future)

    plt.plot(x_future, y_future, label=f'Order {deg}')

# Final plot adjustments
plt.title('Polynomial Fits for UK Population (1950–2025)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()