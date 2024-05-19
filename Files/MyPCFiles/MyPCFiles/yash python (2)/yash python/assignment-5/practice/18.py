#18. Write a Python function to get a string made of the first three characters of a specified string. 
#If the length of the string is less than 3, return the original string.
#Sample function and result :
#first_three('ipy') -> ipy
#first_three('python') -> pyt
def first_three(a:str):
    if len(a)>=3:
        return a[0:3]
    else:
        return a
a=input("enter string: ")
print(first_three(a))