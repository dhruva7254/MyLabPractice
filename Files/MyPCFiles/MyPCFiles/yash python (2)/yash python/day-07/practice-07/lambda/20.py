#20. Write a Python program to find the numbers in a given string and store them in a list. Afterward, 
#display the numbers that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
s="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
#Numbers in sorted form:
#20 23 56
l1=list(filter(lambda x:x.isnumeric(),s.split(" ")))
print(l1)
l2=sorted(map(lambda x:int(x),filter(lambda X:int(X)>len(l1),l1)),key=lambda x:x,reverse=False)
print(l2)
