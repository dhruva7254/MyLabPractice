#13. Write a Python program to count the same pair in two given lists. use map() function.
l1=[1, 2, 3, 4, 5, 6, 7, 8]
l2=[2, 2, 3, 1, 2, 6, 7, 9]
l=list(filter(lambda x:x in l2,l1))
print(len(l),l) 