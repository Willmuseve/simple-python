# A  program that prints if a given year was (or will) be a leap year.
#

print("Please enter a year: ")
year = int(input())

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")