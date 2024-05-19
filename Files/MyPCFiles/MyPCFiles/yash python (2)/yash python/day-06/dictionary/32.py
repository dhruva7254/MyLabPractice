#32. Write a Python program to print a dictionary line by line.
#Ex. 
d={'S001': ['Math', 'Science'], 'S002': ['Math', 'English'], 'S3':['English']}
#o/p 
#'S001':['Math', 'Science']
#'S002':['Math', 'English']
#'S3':['English']
for key in d:
    print(key,d[key],sep=":")