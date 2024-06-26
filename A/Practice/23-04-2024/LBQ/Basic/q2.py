
# Scientific Calculator program

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number is not allowed."
    else:
        return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    elif choice in ('6', '7', '8', '9'):
        num = float(input("Enter the number: "))
        
        if choice == '6':
            print("Result:", sqrt(num))
        elif choice == '7':
            print("Result:", sin(num))
        elif choice == '8':
            print("Result:", cos(num))
        elif choice == '9':
            print("Result:", tan(num))
    else:
        print("Invalid input")
