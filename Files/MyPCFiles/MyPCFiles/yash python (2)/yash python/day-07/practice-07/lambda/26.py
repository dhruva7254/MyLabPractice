#26. Write a Python program to find a list with maximum and minimum length using lambda.
#Original list:
l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#List with maximum length of lists:
#(3, [13, 15, 17])
#List with minimum length of lists:
#(1, [0])
l=sorted(l,key=lambda x:len(x),reverse=True)
print(f"List with maximum length of lists:{(len(l[0]),l[0])}")
print(f"List with maximum length of lists:{(len(l[len(l)-1]),l[len(l)-1])}")