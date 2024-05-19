#15. Write a Python function to create an HTML string with tags around the word(s).
#Sample function and result :
#add_tags('i', 'Python') -> '<i>Python</i>'
#add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def function1(a:str,b:str):
    c="<"+a+">"+b+"</"+a+">"
    return c
a=input("enter first string: ")
b=input("enter second string: ")
print(function1(a,b))