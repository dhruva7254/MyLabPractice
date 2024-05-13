# 33) WAP to convert decimal no to binary without using builtin methods

def decimal_to_binary(decimal):
    # If the decimal number is 0, return '0' as binary representation
    if decimal == 0:
        return '0'
    
    binary = ""  # Initialize an empty string to store the binary representation
    
    # Convert positive decimal number to binary
    while decimal > 0:
        # Get the remainder when dividing by 2 (which gives the least significant bit)
        remainder = decimal % 2
        # Concatenate the remainder to the binary string
        binary = str(remainder) + binary
        # Divide the decimal number by 2
        decimal //= 2
    
    return binary

# Input a decimal number from the user
decimal_number = int(input("Enter a decimal number: "))

binary_representation = decimal_to_binary(decimal_number)

print("Binary representation of", decimal_number, "is:", binary_representation)
