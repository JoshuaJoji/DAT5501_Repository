import numpy as np

def date_diff_calculator(user_date):
    today = np.datetime64('today')
    input_date = np.datetime64(user_date)
    day_diff = (input_date - today).astype(int)
    return day_diff

if __name__ == "__main__":
    user_date = input("Enter a date (YYYY-MM-DD): ")
    day_diff = date_diff_calculator(user_date)
    print(f"The difference in days is: {day_diff} days")