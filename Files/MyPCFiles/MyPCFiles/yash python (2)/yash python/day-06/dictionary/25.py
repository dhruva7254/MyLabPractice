#25. Write a Python program to print a dictionary in table format.
d={'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
for key in d:
    print(key,d[key],sep=" ")