#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
#also create a lambda function that multiplies argument x with argument y and prints the result.
#Sample Output:
#25
#48
def functionp1(a,b):
    c=(lambda x,y:x*y)(a,b)
    return c
def functionp2(a):
    c=(lambda x:x+15)(a)
    return c
print(functionp1(7,8))
print(functionp2(5))