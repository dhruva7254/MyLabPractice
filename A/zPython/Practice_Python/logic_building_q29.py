# 29) Write a  program that takes three numbers as input then print maximum and minimum number of the 
# three

def find_max_min(num1, num2, num3):
    # Find the maximum number
    maximum = max(num1, num2, num3)
    # Find the minimum number
    minimum = min(num1, num2, num3)
    return maximum, minimum

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum and minimum using the find_max_min function
maximum, minimum = find_max_min(num1, num2, num3)

# Print the maximum and minimum numbers
print("Maximum number among", num1, ",", num2, "and", num3, "is:", maximum)
print("Minimum number among", num1, ",", num2, "and", num3, "is:", minimum)
