import numpy as np
import pandas as pd
import os

def date_diff_calculator(user_date):
    today = np.datetime64('today')
    try:
        input_date = np.datetime64(user_date)
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    day_diff = (input_date - today).astype(int)
    return day_diff

def calculate_csv(file_name="random_dates.csv"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, file_name)

    df = pd.read_csv(csv_path, header=None, names=["date"])
    df['Days_Difference'] = df['date'].apply(date_diff_calculator)
    print(df)

if __name__ == "__main__":
    user_date = input("Enter a date (YYYY-MM-DD): ")
    day_diff = date_diff_calculator(user_date)
    print(f"The difference in days is: {day_diff} days")

    calculate_csv("random_dates.csv")