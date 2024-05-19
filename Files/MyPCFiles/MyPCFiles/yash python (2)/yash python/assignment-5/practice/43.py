#43. Write a Python program to print the square and cube symbols in the area of a 
#rectangle and the volume of a cylinder.
#Sample output:
#The area of the rectangle is 1256.66cm2
#The volume of the cylinder is 1254.725cm3
# Define the area and volume as floating-point numbers.
area = 1256.66
volume = 1254.725

# Define the number of decimals for formatting.
decimals = 2

# Print the area of the rectangle with formatting and the specified number of decimals.
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))

# Update the number of decimals for formatting.
decimals = 3

# Print the volume of the cylinder with formatting and the specified number of decimals.
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))