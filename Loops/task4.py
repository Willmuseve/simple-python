#  A program that prints the multiplication table for a positive integer n.
# Values displayed go from n x 1 up to n x 10 with a descriptive format

n = int(input("Enter the value of n: "))

print(f"====== The miltiplication table of {n} is : ======")

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")