#58. Write a Python program to move spaces to the front of a given string.
s=input("enter string: ")
s1=""
for e in s:
    if e==" ":
        s1=s1+e
s1=s1+"".join(s.split(" "))
print(s1)
    