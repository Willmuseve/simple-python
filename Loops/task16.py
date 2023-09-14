# A program that prints a diamond made with asterisks where the diamond's height
# (number of rows) is determined by the value of the variable height

height = int(input("Enter an odd number"))

if height % 2 == 0:
    print("Please enter an odd number.")
else:
    middle_rows = (height+2) // 2

    for i in range(middle_rows):
        print(" " * (middle_rows-i), "*" * (i *2 + 1))
    for i in range(middle_rows-2, -1, -1):
        print(" " * (middle_rows-i), "*" * (i *2 + 1))