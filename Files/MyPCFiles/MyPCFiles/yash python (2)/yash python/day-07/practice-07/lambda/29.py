#29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
#Original list:
l=['Python', 3, 2, 4, 5, 'version']
#Maximum values in the said list using lambda:
#5
print(max(list(filter(lambda x:str(x).isnumeric(),l))))
