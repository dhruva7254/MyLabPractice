# 27) Write a  program to print the area and perimeter of a circle

import math

def calculate_circle(radius):
    # Calculate area of the circle
    area = math.pi * radius ** 2
    # Calculate perimeter (circumference) of the circle
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Input radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter using the calculate_circle function
area, perimeter = calculate_circle(radius)

# Print the results
print(f"Area of the circle with radius {radius} is: {area}")
print(f"Perimeter (circumference) of the circle with radius {radius} is: {perimeter}")
