#34. Write a Python program to count the total number of items under all keys in a dictionary value that is a list.
#Ex. 
d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
#o/p total values : 5
s=0
for key in d:
  s=s+len(d[key])
print(f"total values:{s}")  