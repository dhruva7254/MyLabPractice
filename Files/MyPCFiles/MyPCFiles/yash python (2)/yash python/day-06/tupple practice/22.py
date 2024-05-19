#22. Write a Python program to remove an empty tuple(s) from a list of tuples.
data=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
data1=[e for e in data if len(e)!=0]
print(data1)        