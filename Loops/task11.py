# A program that prints the digits of a number in reverse order on the same line.


number  = int(input("Enter a given number: "))

reverse = int(str(number)[::-1])
print(reverse)



print("\nMethod 2:")
reversed_num = 0

while number  > 0:
    remainder = number % 10
    reversed_num = (reversed_num * 10) + remainder
    number = number // 10

print(reversed_num)