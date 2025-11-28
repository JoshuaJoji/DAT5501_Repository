import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "amazon_historical_nasdaq.csv")
df = pd.read_csv(csv_path)

#df = pd.read_csv('amazon_historical_nasdaq.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df = df.sort_values(by='Date', ascending=True)

pd.set_option('display.max_rows', None)

df['Close/Last'] = df['Close/Last'].replace('[\$,]', '', regex=True).astype(float)
df['Daily Price Change'] = df['Close/Last'].diff()

print(df)

price_changes = df['Daily Price Change'].dropna().to_numpy()
times = []

for i in range(7, len(price_changes)):
    
    array_to_sort = price_changes[:i]
    
    start_time = time.perf_counter()
    sorted_array = sorted(array_to_sort)
    end_time = time.perf_counter()
    
    time_taken = end_time - start_time
    times.append(time_taken)

x_values = np.arange(7, len(times)+7)
n_log_n = x_values * np.log(x_values) 
n_log_n = n_log_n / np.max(n_log_n) * np.max(times)#normalise

plt.figure(figsize=(8, 4))
plt.plot(x_values, times, linestyle='-', color='blue')
plt.plot(x_values, n_log_n, label='n log n', color='red')
plt.legend()

plt.title('Daily Price Changes to Sort vs Sorting Time')
plt.xlabel('Number of Price Changes Sorted')
plt.ylabel('Time')
plt.grid(True)
plt.tight_layout()
plt.show()