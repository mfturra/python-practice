# Goal: Calculate area of circle based on radius input from user
# Import library
import math

# Gather input from user
radius = float(input("Radius of circle: "))
pi = float(math.pi)

# Calculate area based on input radius from user
area = round(pi*radius**2, 2)

# Print output for user
print("Area: ", area)
