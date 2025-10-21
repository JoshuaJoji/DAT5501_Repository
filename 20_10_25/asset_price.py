import pandas as pd

df = pd.read_csv('amazon_historical_nasdaq.csv')
print(df.head())
df['Close/Last'] = pd.to_numeric(df['Close/Last'].str.replace('$', '').str.replace(',', ''), errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

import matplotlib.pyplot as plt

plt.plot(df['Date'], df['Close/Last'], label='AMZN Closing Price')
plt.title('Amazon (AMZN): 1 Year Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

df['Daily % Change'] = df['Close/Last'].pct_change() * 100
plt.plot(df['Date'], df['Daily % Change'], label='Daily % Change', color='orange')
plt.title('Amazon (AMZN): Daily % Change in Price')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid(True)
plt.show()

std_dev = df['Daily % Change'].std()
print(f'Standard Deviation of Daily % Change: {std_dev:.2f}%')