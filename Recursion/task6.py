# A python program that prints the GCD of of given numbers

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(4, 2))