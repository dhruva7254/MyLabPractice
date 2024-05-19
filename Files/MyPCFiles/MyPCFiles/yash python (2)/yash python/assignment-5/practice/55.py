#55.Write a Python program to find the first repeated word in a given string.
s=input("enter string: ")
c=0
for e in s.split(" "):
    if s.count(e)>1:
        print(e)
        break
    c=c+1
if c==len(s.split(" ")):
    print("No repeted word")
