# A python program that prints the number of days in a given month
# The value of the variable month is the name of the variable month with the first letter capitalised
# Exclude leap years in the month of february

print("Enter month:")
month_entered = str(input())

month_28days = "February"
month_31days = ("January", "March", "May", "July", "August", "October", "December" )
month_30days = ("April", "June", "September", "November")

if month_entered in month_28days:
    print(f"{month_entered} has 28 days")
elif month_entered in month_30days:
    print(f"{month_entered} has 30 days")
elif month_entered in month_31days:
    print(f"{month_entered} has 31 days")
else:
    print("Invalid input! Please try again")