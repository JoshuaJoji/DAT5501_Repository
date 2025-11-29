import speedtest
import pandas as pd
from datetime import datetime
import time
import os

proj_folder = "Projects/internet_speed_tracker"

# Function to run speed test and return results
def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = st.download() / 1_000_000  #Mbps
    upload = st.upload() / 1_000_000      #Mbps
    ping = st.results.ping

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "Time": now,
        "Download_Mbps": round(download, 2),
        "Upload_Mbps": round(upload, 2),
        "Ping_ms": round(ping, 2)
    }

# Function to save results to CSV
def save_to_csv(data, filename="speed_log.csv"):
    filepath = os.path.join(proj_folder, filename)
    df = pd.DataFrame([data])

    try:
        existing = pd.read_csv(filename)
        df = pd.concat([existing, df], ignore_index=True)
    except FileNotFoundError:
        pass  #First time

    df.to_csv(filename, index=False)

# Main loop to run the speed test at intervals
def main(interval_minutes=30):
    print("Internet Speed Tracker Started...\n")

    while True:
        result = run_speed_test()
        save_to_csv(result)

        print(f"[{result['Time']}] ↓ {result['Download_Mbps']} Mbps | ↑ {result['Upload_Mbps']} Mbps | Ping {result['Ping_ms']} ms")

        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    main(interval_minutes=30)