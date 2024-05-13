# 28) Write a  program that takes three numbers as input to calculate and print the average of the 
# numbers.

def calculate_average(num1, num2, num3):
    # Calculate the average of the three numbers
    average = (num1 + num2 + num3) / 3
    return average

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average using the calculate_average function
average = calculate_average(num1, num2, num3)

# Print the average
print("The average of", num1, ",", num2, "and", num3, "is:", average)
