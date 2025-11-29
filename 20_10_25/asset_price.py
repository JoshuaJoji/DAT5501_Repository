import pandas as pd
import os
import matplotlib.pyplot as plt

# Load data from 10_11_25 directory
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.abspath(os.path.join(script_dir, "..", "10_11_25", "amazon_historical_nasdaq.csv"))
df = pd.read_csv(csv_path)
print(df.head())

# Clean and process
df['Close/Last'] = pd.to_numeric(df['Close/Last'].str.replace('$', '').str.replace(',', ''), errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Plot closing prices
plt.plot(df['Date'], df['Close/Last'], label='AMZN Closing Price')
plt.title('Amazon (AMZN): 1 Year Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Daily % change
df['Daily % Change'] = df['Close/Last'].pct_change() * 100
plt.plot(df['Date'], df['Daily % Change'], color='orange', label='Daily % Change')
plt.title('Amazon (AMZN): Daily % Change in Price')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.show()

# Standard deviation
std_dev = df['Daily % Change'].std()
print(f'Standard Deviation of Daily % Change: {std_dev:.2f}%')