# Calendar Printer
# This program prints a simple calendar for a month based on user input.

print("How many days in your month?")
days_in_month = int(input())

# Validate the number of days
while True:
    print("What day of the week does your month start on? s = 0, m = 1, t = 2...")
    start_day = int(input())
    if 0 <= start_day <= 6:
        break
    else:
        print("Invalid input. Please enter a number between 0 and 6.")

print("S  M  T  W  T  F  S")

# Print leading spaces for the first week
current_day = 1
for space in range(start_day):
    print("--", end=" ")
    current_day += 1

for day in range(1, days_in_month + 1):
    if current_day % 7 == 0:
        print(day)
    elif day < 9:
        print(day, end="  ")
    else:
        print(day, end=" ")
    current_day += 1