# 32) Write a  program to add and multiply two binary numbers

def binary_addition(bin1, bin2):
    # Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    # Perform addition
    result = num1 + num2
    # Convert the result back to binary and return
    return bin(result)[2:]

def binary_multiplication(bin1, bin2):
    # Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    # Perform multiplication
    result = num1 * num2
    # Convert the result back to binary and return
    return bin(result)[2:]

# Example binary numbers
binary_num1 = "1010"
binary_num2 = "1101"

# Perform addition
addition_result = binary_addition(binary_num1, binary_num2)
print("Addition result:", addition_result)

# Perform multiplication
multiplication_result = binary_multiplication(binary_num1, binary_num2)
print("Multiplication result:", multiplication_result)
