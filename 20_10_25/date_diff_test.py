import numpy as np
import pytest

from duration_calculator import date_diff_calculator

# Test cases for date_diff_calculator function
def test_future_date():
    future_date = '2030-10-14'
    #future_date = '1990-12-31'
    expected_diff = (np.datetime64(future_date) - np.datetime64('today')).astype(int)
    assert date_diff_calculator(future_date) == expected_diff
    assert expected_diff > 0

# Test for past date
def test_past_date():
    past_date = '2000-09-21'
    #past_date = '2050-01-01'
    expected_diff = (np.datetime64(past_date) - np.datetime64('today')).astype(int)
    assert date_diff_calculator(past_date) == expected_diff
    assert expected_diff < 0

# Test for today's date
def test_today_date():
    today_date = str(np.datetime64('today'))
    #today_date = '2024-06-15'
    expected_diff = 0
    assert date_diff_calculator(today_date) == expected_diff

# Test for invalid date format
def test_invalid_date_format():
    with pytest.raises(ValueError):
        date_diff_calculator('20-10-25')#invalid format
    with pytest.raises(ValueError):
        date_diff_calculator('2027-13-01')#invalid month
    with pytest.raises(ValueError):
        date_diff_calculator('2025/10/23')#wrong separator
    assert isinstance(date_diff_calculator('2025-02-25'), int)
    assert isinstance(date_diff_calculator('2024-01-10'), int)
    assert isinstance(date_diff_calculator('2029-06-25'), int)

if __name__ == "__main__":
    test_future_date()
    test_past_date()
    test_today_date()
    test_invalid_date_format()
    print("All tests passed.")