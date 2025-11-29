# Compound Interest Calculator

def compound_interest(savings, annual_rate, years): # savings: initial amount, annual_rate: decimal, years: number of years
    amount = savings
    doubled_year = None

    print(f"Initial savings: £{savings:.2f}")
    print(f"Annual interest rate: {annual_rate * 100:.1f}%")

    for year in range(1, years + 1):# Loop through each year
        amount *= (1 + annual_rate)
        print(f"Year {year}: £{amount:.2f}")

        if doubled_year is None and amount >= savings * 2:
            doubled_year = year
            
    if doubled_year:# If savings doubled within the time
        print(f"The savings double after **{doubled_year} years**.")
    else:
        print("The savings did NOT double within the given time.")

    return doubled_year

print("Enter the initial savings amount: £")
savings = float(input())

print("Enter the annual interest rate (as a PERCENT, e.g. 5 for 5%): ") # Input as percent
annual_rate_percent = float(input())
annual_rate = annual_rate_percent / 100 #convert to decimal

print("Enter the number of years: ")# Input number of years
years = int(input())

compound_interest(savings, annual_rate, years)