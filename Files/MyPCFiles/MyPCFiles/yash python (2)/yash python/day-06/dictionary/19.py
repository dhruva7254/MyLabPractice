#19. Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'c': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d={}
for k1 in d1:
    for k2 in d2:
        if k1==k2:
            d[k1]=d1[k1]+d2[k2]
for kd in d2:
    if kd not in d:
        d[kd]=d2[kd]      
for k in d1:
    if k not in d:
        d[k]=d1[k]     
print(d)        
