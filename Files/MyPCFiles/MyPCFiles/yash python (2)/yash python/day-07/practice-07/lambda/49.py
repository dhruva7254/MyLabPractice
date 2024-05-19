#49. Write a Python program to count the occurrences of items in a given list using lambda.
#Original list:
l=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
#Count the occurrences of the items in the said list:
#{3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}
l1=list(map(lambda x:l.count(x),l))
d=dict(zip(l,l1))
print(d)