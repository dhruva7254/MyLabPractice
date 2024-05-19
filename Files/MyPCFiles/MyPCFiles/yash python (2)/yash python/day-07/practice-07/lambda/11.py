#11. Write a Python program to find the intersection of two given arrays using Lambda.
#Original arrays:
a1=[1, 2, 3, 5, 7, 8, 9, 10]
a2=[1, 2, 4, 8, 9]
#Intersection of the said arrays: [1, 2, 8, 9]
i=lambda x,y:sorted(list(set(x)&set(y)),key=lambda x:x,reverse=False)
print(i(a1,a2))