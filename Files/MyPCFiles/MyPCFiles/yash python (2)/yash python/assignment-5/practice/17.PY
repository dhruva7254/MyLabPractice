#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#Sample function and result :
#insert_end('Python') -> onononon
#insert_end('Exercises') -> eseseses
def insert_end(a:str):
    if len(a)>=2:
        s1=a[len(a)-2:len(a)]*4
        return s1
    else:
        print("enter string with at least 2 charaters")
a=input("enter string: ")
print(insert_end(a))        