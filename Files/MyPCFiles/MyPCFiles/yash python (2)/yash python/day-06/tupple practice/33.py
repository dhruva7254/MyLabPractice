#33. Write a Python program to convert a given list of tuples to a list of lists.
#l1=[(1, 2), (2, 3), (3, 4)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
l1=[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
for idx in range(len(l1)):
    l1[idx]=list(l1[idx])
print(l1)

