#36. Write a Python program to extract the nth element from a given list of tuples using lambda.
#Original list:
l=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
#Extract nth element ( n = 0 ) from the said list of tuples:
#['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
#Extract nth element ( n = 2 ) from the said list of tuples:
#[99, 96, 94, 98]
n=int(input("enter element no: "))
print(list(map(lambda x:x[n],l)))