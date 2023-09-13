# A python program that determines if three numbers are in ascending order or descending

print("Enter the first number:")
num1 = int(input())


print("Enter the second number:")
num2 = int(input())


print("Enter the third number:")
num3 = int(input())



if num1  > num2 > num3:
    print("Numbers are in Descending order")
elif num1 < num2 < num3:
    print("Numbers are in Ascending Order")
else:
    print("None")
