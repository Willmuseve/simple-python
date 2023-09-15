# A program to print a pattern of asterics

def asterics(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        asterics(n-1)


print(asterics(7))