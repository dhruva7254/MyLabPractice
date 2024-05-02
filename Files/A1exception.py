
# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

"""try:
    a = 5
    print(5//0)   # ZeroDivisionError: integer division or modulo by zero
except ZeroDivisionError:
    print("integer division is not possible by zero")"""

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception 
# if the input is not a valid integer.

"""try:
    a = int(input("Enter an integer value: ")) # 6.0
    print(a)   # ValueError: invalid literal for int() with base 10: '6.0'
except ValueError:
     print("invalid literal for int() with base 10: '6.0'")"""

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does 
# not exist.

"""try:
    f=open("sample_file.py")   # FileNotFoundError: [Errno 2] No such file or directory: 'sample_file.py'
    print(f.read())
    f.close()
except FileNotFoundError:
    print("No such file or directory: 'sample_file.py'")"""

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

# Advanced::
"""print("Enter 2 numbers")
try:
    num1 = int(input("Enter 1st number: "))
    num2 = input("Enter 2nd number: ")
    print(num1 + num2)
except TypeError:
    print("cannot add two different data types")
except Exception as e:
    raise e"""

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
"""try:
    f = open("D:\Dhruva\sample_file.txt")
except PermissionError:
    print("not permitted to write in file")"""

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
"""l1 = ['a','b','c','d','e','f']
try: 
    print(l1[8])
except IndexError:
    print("Cannot access beyond range of list. please enter valid index")"""



# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
"""try:
    num = float(input("Enter a nmber: "))
except KeyboardInterrupt:
    print("Enter number not 'Ctrl+c' ")"""


# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
"""try:
    a = 5
    print(5//0) #ArithmeticError is base of ZeroDivisionError
except ArithmeticError:
    print("integer division is not possible by zero")
"""

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.


# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    list.decode("utf-8")
except AttributeError:
    print("type object 'list' has no attribute 'decode'")

