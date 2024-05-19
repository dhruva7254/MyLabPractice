#2. Write a Python program to add three given lists using Python map and lambda.
l1=[1, 2, 3]
l2=[8, 9, 10]
l3=[4, 5, 6, 7]
l=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(l)
