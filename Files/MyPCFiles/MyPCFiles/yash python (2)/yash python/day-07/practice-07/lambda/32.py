#32. Write a Python program to count float values in a mixed list using lambda.
#Original list:
l=[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
#Number of floats in the said mixed list:
#3
print(len(list(filter(lambda x:type(x)==float,l))))