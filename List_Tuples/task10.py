# A python program that calculates the distance between two 3d points
# points are represented by two lists wit 3 elements: x-coordinate, y-coordinarte and z coordinate

# Method 1: 
print("Method 1:")
a = [2, 4, 5] 
b = [2, 4, 5]

distance = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2 ) ** (1/2)
print(distance)
print("\n")


#Method 2:
print("Method 2: Using math module")

import math

c = [1, 2, 3]
d = [4, 5, 6]

add = ((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2 + (c[2] - d[2]))

distance2 = math.sqrt(add)
print(distance2)