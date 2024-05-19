#28. Write a Python program. There is a dictionary where values contain list of integers.
#So, program should sort that list and return complete dictionary
#Ex. 
#i/p
d={'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
#o/p
#{'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
l1=list(d.keys())
l2=list(d.values())
l3=[]
for e in l2:
    l3.append(sorted(e,key=lambda x:x))
d1=dict(zip(l1,l3))
print(d1)
