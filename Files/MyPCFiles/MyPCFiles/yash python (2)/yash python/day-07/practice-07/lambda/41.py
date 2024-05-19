#41. Write a Python program to reverse strings in a given list of string values using lambda.
#Original lists:
l=['Red', 'Green', 'Blue', 'White', 'Black']
#Reverse strings of the said given list:
#['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
print(list(map(lambda x:x[::-1],l)))
