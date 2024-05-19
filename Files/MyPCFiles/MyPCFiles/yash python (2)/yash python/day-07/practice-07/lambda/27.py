#27. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
#Original list:
l=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
#After sorting each sublist of the said list of lists:
#[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
print(list(map(lambda x:sorted(x,key=lambda a:a,reverse=False),l)))