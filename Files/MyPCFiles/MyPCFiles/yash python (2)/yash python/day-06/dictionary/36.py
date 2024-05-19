#36. Write a Python program to create a dictionary from two lists without losing duplicate values.
l1=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
l2=[1, 2, 2, 3]
d={}
a=set()
for e1,e2 in zip(l1,l2):
    a.add(e2)
    d[e1]=a
    a=set()
print(d)    

         
