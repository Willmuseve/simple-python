# A program that prints the factorial of a given number n
# The value of n is entered by the user

n = int(input("Enter the value of n: "))

factorial = 1
for i in range(2, n+1):
    factorial*=i
print(factorial)