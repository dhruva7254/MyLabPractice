#40. Write a Python program to find the nested list elements, which are present in another list using lambda.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,18]
l1=[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
#Intersection of said nested lists:
#[[12], [7, 11], [1, 5, 8]]
print(list(map(lambda x:(list(filter(lambda x1:x1 in l,x))),l1)))