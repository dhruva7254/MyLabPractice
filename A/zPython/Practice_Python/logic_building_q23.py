# 23) Take a number from user. Print highest number possible using all digits once from given number

def highest_number_from_digits(num):
    # Convert the number to a string and then to a list of digits
    digits = list(str(num))
    
    # Sort the digits in descending order
    sorted_digits = sorted(digits, reverse=True)
    
    # Concatenate the sorted digits to form the highest number
    highest_num = int(''.join(sorted_digits))
    
    return highest_num

# Input from the user
num = int(input("Enter a number: "))

# Calculate and print the highest number
print("Highest number using all digits once:", highest_number_from_digits(num))
