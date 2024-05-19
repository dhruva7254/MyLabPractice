#7. Write a Python program to add two given lists and find the difference between them. Use the map() function.
l1=[10, 15, 20, 25, 30, 35, 40]
l2=[25, 40, 35]
la=list(map(lambda x:l1.append(x),l2))
print(l1)
l1=[10, 15, 20, 25, 30, 35, 40]
ls=list(filter(lambda x:x not in l2,l1))
print(ls)
