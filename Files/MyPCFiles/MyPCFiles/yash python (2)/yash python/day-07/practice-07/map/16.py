#16. Write a Python program to convert a given list of strings into a list of lists using the map function.
l=['Red', 'Green', 'Black', 'Orange']
l1=list(map(lambda x:list(x),l))
print(l1)
