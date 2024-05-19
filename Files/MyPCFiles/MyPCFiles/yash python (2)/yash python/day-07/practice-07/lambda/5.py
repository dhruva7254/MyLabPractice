#5. Write a Python program to filter a list of integers using Lambda.
#Original list of integers:
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Even numbers from the said list:
#[2, 4, 6, 8, 10]
#Odd numbers from the said list:
#[1, 3, 5, 7, 9]
print(list(filter(lambda x:x%2==0,l)))
print(list(filter(lambda x:x%2!=0,l)))
#print([e for e in l if e%2==0])
#print([e for e in l if e%2!=0])
