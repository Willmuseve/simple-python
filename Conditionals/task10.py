# A program that stimulates an interactive calculator with the basic arithmetic operations
# Interacts with the user

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

print("=====Welcome to your first interaction python session =====")
a = int(input("Enter your first value: "))
b = int(input("Enter your first value: "))


print("Now Enter the operations to be performed")
print("Choose between these options:")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = Integer division")
print("6 = Modulo")

Operator = int(input("Enter the operator to be used: "))

if Operator == ADDITION:
    result = a + b
    print(f"The sum of {a} + {b} is: {result}")
elif Operator == SUBTRACTION:
    result = a - b
    print(f"The subtraction of {a} - {b} is :{result}")
elif Operator == MULTIPLICATION:
    result = a * b
    print(f"The multiplication of {a} * {b} is: {result}")
elif Operator == DIVISION:
    result = a / b
    print(f" The division of {a} / {b} is : {result}")
elif Operator == INTEGER_DIVISION:
    result = a//b
    print(f" The integer division of {a} and {b} is: {result}")
elif Operator == MODULO:
    print(f" The modulo of {a} and {b}")
else:
    print("please enter a valid operation")