import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("speed_log.csv")

plt.figure(figsize=(12, 6))
plt.plot(df["Time"], df["Download_Mbps"], label="Download")
plt.plot(df["Time"], df["Upload_Mbps"], label="Upload")
plt.xticks(rotation=45)
plt.ylabel("Mbps")
plt.title("Internet Speed Over Time")
plt.legend()
plt.tight_layout()
plt.show()