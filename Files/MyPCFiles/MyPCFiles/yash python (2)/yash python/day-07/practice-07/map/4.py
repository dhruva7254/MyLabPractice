#4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in 
#the index using Python map.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=int(input("enter power: "))
print(list(map(lambda x:x**n,l)))