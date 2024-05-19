#23. Write a Python program to remove a newline in Python.
s=input("enter string: ")
a=str(input("enter forword slash: "))
if "\n" in s:
    s1=""
    for e in s:
        if (e!="n")&(e!=a):
           s1=s1+e
           print(s1)
    print(s1)
else:
    print(s)           


        

