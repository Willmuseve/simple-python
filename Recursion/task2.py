# A python program that calculates and print the nth fibonnacci number
# The value of n(An initial value of 0) reps the position of the number

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(6))