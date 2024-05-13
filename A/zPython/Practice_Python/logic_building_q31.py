# 31) Write a  program to swap two variables
#     a. by using a temporary variable
#     b. using arithmatic operation and not using a variable
#     c. without using variable ( using python unpacking syntax)

# a. by using a temporary variable

def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage:
x = 5
y = 10
x, y = swap_with_temp(x, y)
print("After swapping using a temporary variable:")
print("x =", x)
print("y =", y)

# b. using arithmatic operation and not using a variable

def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage:
x = 5
y = 10
x, y = swap_without_temp(x, y)
print("After swapping using arithmetic operations without a variable:")
print("x =", x)
print("y =", y)

# c. without using variable ( using python unpacking syntax)

def swap_without_variable(a, b):
    return b, a

# Example usage:
x = 5
y = 10
x, y = swap_without_variable(x, y)
print("After swapping without using a variable (using Python unpacking syntax):")
print("x =", x)
print("y =", y)
