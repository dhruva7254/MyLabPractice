#37. Write a Python program to replace dictionary values with their sums.
d={'Class-V': {1,2,4}, 'Class-VI': {2,4,5}, 'Class-VII': {2,2}, 'Class-VIII': {3,4}}
for key in d:
    s=0
    a=set()
    for e in d[key]:
        s=s+e
    a.add(s)
    d[key]=a
print(d)        
