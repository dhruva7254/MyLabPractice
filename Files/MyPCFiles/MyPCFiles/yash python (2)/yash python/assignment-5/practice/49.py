#49. Write a Python program to count and display vowels in text.
v="aeiou"
s=input("enter string: ")
c=0
l=[]
for e in v:
    if e in s:
        l.append(e)
    c=c+s.count(e)
print(c,l)
