#27. Write a Python program to convert a list into a nested dictionary of keys.
l=[1, 2, 3, 4]
#o/p  {1: {2: {3: {4: {}}}}}
a=d={}
for e in l:
    d[e]={}
    print(d)
    d=d[e]
    print(d)
print(a)  



