#29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.
l=[1,2,3,4,1,2,6,5,4,7,8,9,12,3,6]
n=int(input("enter which largest no to find: "))
print(sorted(set(l),key=lambda x:x,reverse=True)[n-1])
