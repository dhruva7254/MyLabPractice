#17. Write a Python program to convert a given list of tuples to a list of strings using the map function.
#Original list of tuples:
l=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
#Convert the said list of tuples to a list of strings:
#['red pink', 'white black', 'orange green']
l1=list(map(lambda x:x[0]+" "+x[1],l))
print(l1)