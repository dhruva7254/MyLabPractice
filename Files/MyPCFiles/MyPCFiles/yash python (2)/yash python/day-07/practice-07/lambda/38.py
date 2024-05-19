#38. Write a Python program to remove all elements from a given list present in another list using lambda.
#Original lists:
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2=[2, 4, 6, 8]
#Remove all elements from 'list1' present in 'list2:
#[1, 3, 5, 7, 9, 10]
l=list(map(lambda x:l1.remove(x),l2))
print(l1)
print(l)