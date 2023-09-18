# A progam that finds the area of a circle from the value of the diameter d
# round off the result to two decimal places

import math

diameter = int(input("Enter the diameter:"))

radius = diameter /2
area = round(math.pi * (radius**2), 2)

print(f"The area of the circle with diameter {diameter} is {area}")