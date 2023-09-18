# A program that computes the area of a triangle  from it's base and height
# prints the area to two decimal places
# the values of the base and height should be entered by the user
# The program prints "Please enter valid values for base and height" if either one of the values is invalid

base  = int(input("Enter the base:"))
height = int(input("Enter the height: "))

if base > 0 and height > 0:
    area = round((base * height) / 2, 2)
    print(f" The area of the tringle is {area}")
else:
    print("Please enter the correct value base or height")