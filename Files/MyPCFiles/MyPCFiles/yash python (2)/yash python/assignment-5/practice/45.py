#45. Write a Python program to check whether a string contains all letters of the 
#alphabet[a-z].
a="abcdefghijklmnopqrstuvwxyz"
s=input("enter string: ")
c=0
for e in a:
    if e not in s:
        print("string do not contains all letters of the alphabet")
        break
    else:
        c=c+1
if c==26:
    print("string contains all letters of the alphabet")
    