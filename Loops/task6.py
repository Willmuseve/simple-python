# A program that prints the firt 100 even nums

for i in range(1, 201):
    if i % 2 == 0:
        print(i)


# Method 2
print("\nMethod 2:")
for i in range(2, 201, 2):
    print(i)