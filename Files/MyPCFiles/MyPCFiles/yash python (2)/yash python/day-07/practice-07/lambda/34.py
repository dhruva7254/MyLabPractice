#34. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.
#Original Dictionary:
d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
#Height> 6ft and Weight> 70kg:
#{'Cierra Vega': (6.2, 70)}
print(dict(filter(lambda x:(x[1][0]==6.2)&(x[1][1]==70),d.items())))