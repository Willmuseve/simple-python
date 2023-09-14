# A python program that checks if a number is prime
# Prints prime if the number is prime else not prime

num  = int(input("Enter an integer: "))


if num == 0 or num == 1:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")