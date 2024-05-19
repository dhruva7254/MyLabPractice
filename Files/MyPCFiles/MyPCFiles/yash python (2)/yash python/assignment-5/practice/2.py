#2. Write a Python program to get character frequency of every character in a string.
#Sample String : google.com
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
s=input("enter string ")
a=set(list(s))
d={}
for e in a:
    d[e]=s.count(e)
print(d)