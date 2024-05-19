#41. Write a Python program to drop empty items from a given dictionary.
#Original Dictionary:
d={'c1': 'Red', 'c2': None, 'c3':'Green'}
#New Dictionary after dropping empty items:
#{'c1': 'Red', 'c2': 'Green'}
d1=d.copy()
for key in d1:
    if d1[key]==None:
        del d[key]
print(d)        