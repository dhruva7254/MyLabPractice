# 30) Write a  program and compute the sum of the digits of an integer.

def sum_of_digits(n):
    # Initialize sum to 0
    digit_sum = 0
    # Iterate over each digit in the number
    while n > 0:
        # Extract the last digit
        digit = n % 10
        # Add the digit to the sum
        digit_sum += digit
        # Remove the last digit from the number
        n //= 10
    return digit_sum

# Input an integer from the user
number = int(input("Enter an integer: "))

# Calculate the sum of digits using the sum_of_digits function
result = sum_of_digits(abs(number))  # Take absolute value in case of negative numbers

# Print the result
print("Sum of the digits of", number, "is:", result)
