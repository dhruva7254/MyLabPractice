#53. Write a Python program to find the first repeated character in a given string.
s=input("enter string: ")
c=0
for e in s:
    c=c+1
    if s.count(e)>1:
        print(e)
        break
if c==len(s):
    print("no repeted characters")