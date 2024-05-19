#5. Write a Python program to square the elements of a list using the map() function.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=int(input("enter power: "))
print(list(map(lambda x:x**n,l)))