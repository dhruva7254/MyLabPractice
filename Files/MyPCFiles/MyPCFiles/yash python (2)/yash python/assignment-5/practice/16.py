#16. Write a Python function to insert a string in the middle of a string.
#Sample function and result :
#insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_string_middle(a:str,b:str):
    c=a[0:len(a)//2]+b+a[len(a)//2:len(a)]
    return c
a=input("enter first string: ")
b=input("enter second string: ")
print(insert_string_middle(a,b))
