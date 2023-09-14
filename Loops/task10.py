# A python program that prints a triangular pattern

number = int(input("Enter number: "))

for i in range(1, number+1, 2):
    print("*" * i)
