# A program that prints the smallest of three integers num1, num2, num3

num1 = 4
num2 = 6
num3 = 2

if (num1 <= num2) and (num1 <= num3):
    print(f"{num1} num1")
elif (num2 <=num1) and (num2 <= num3):
    print(f"{num2} num1")
else:
    print(f"{num3} num3")

# Alternatively
print(min(num1, num2, num3))