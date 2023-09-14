# A program that prints a triangular pattern made with letters
# The first  row has one letter A(uppercase), second row has two letter B(uppercase), third row has 3 Cs uppercase and so on


n = int(input("Enter the number of rows: "))


for i in range(n):
    print(chr(65 + i) * (i + 1))