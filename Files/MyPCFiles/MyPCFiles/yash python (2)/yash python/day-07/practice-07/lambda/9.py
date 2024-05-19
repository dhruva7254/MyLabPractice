#9. Write a Python program to check whether a given string is a number or not using Lambda.
a=lambda x:x.replace(".","",1).isdigit()
print(a("02.1.2"))