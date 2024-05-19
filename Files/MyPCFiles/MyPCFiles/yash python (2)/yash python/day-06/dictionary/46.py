#46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
#Original list:
l=[('yellow', 1), ('blue', 5),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#Grouping a sequence of key-value pairs into a dictionary of lists:
#{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
d={}
for e1 in l:
    l1=[]
    for e2 in l:
        if (e1!=e2)&(e1[0]==e2[0]):
         l1.append(e2[1])
         l1.append(e1[1])
        d[e1[0]]=l1
print(d)         