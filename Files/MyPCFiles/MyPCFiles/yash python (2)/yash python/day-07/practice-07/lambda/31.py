#31. Write a Python program to extract a specified size of strings from a given list of string values using lambda.
#Original list:
l=['Python', 'list', 'exercises', 'practice', 'solution']
#length of the string to extract:
#8
#After extracting strings of specified length from the said list:
#['practice', 'solution']
n=int(input("enter length of string: "))
print(list(filter(lambda x:len(x)==n,l)))