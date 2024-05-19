#56. Write a Python program to find the second most repeated word in a given string.
s=input("enter string: ")
se=set(s.split(" "))
d={}
for e in se:
    d[e]=s.count(e)
print(d)
l=sorted(list(d.values()),key=lambda x:x,reverse=True)
print(l)
for a in d:
    if d[a]==l[1]:
        print(f"second most occurance word in string: {a}")
        
    
