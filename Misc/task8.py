# A python program that prints the calender of a given month in a given year
# User to enter the month and theyear
# Displays a descriptive message if the user does not enter a given month or year

import calendar
print("Python's calender")

year = int(input("Enter the year to be printed(YYYY): "))
month = int(input("Enter the month to be pronted(1-12): "))

if (len(str(year)) > 4 or len(str(year))< 4) and month not in range(1, 13):
    print("Please enter the specified formats.")
else:
    print(calendar.month(year, month))