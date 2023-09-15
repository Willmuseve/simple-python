# A python program that converts a decimal to binary
# Returns a binary representation as a string and prints

def binary_decimal(n):
    if n == 0:
        return "0"
    else:
        return (binary_decimal(n//2) + str(n % 2)).lstrip("0")
    

print(binary_decimal(9))