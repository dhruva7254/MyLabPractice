#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    n1=int(input("enter the integer: "))
except ValueError:
    print("enter integer only..")
else:
    print("number is integer..")