# A program that calculates and prints the sum of digits of a positive integer num recursively
# Prints the digit as the sum if the integer has one digit

def sum_of(num):
    if num == 0:
        return 0
    else:
        return(num % 10) + (sum_of (num//10))

print(sum_of(345))