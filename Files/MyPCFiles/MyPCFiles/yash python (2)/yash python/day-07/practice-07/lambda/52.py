#52. Write a Python program to remove None values from a given list using the lambda function.
#Original list:
l=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
#Remove None value from the said list:
#[12, 0, 23, -55, 234, 89, 0, 6, -12]
lr=list(map(lambda x:l.remove(x),list(filter(lambda x:x==None,l))))
print(l)