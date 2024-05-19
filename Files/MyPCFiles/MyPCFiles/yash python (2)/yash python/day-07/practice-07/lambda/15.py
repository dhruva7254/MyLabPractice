#15. Write a Python program to add two given lists using map and lambda.
#Original list:
l1=[1, 2, 3]
l2=[4, 5, 6]
#Result: after adding two list
#[5, 7, 9]
l=list(map(lambda x,y:x+y,l1,l2))
print(l)