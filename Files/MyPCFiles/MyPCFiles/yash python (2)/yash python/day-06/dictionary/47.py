#47. Write a Python program to split a given dictionary of lists into lists of dictionaries.
#Original dictionary of lists:
d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#Split said dictionary of lists into list of dictionaries:
#[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
lv=list(d.values())
lk=list(d.keys())
l=[]
for idx1 in range(len(lk)):
  d={}
  for idx2 in range(len(lv[0])):
   d[lk[idx1]]=lv[idx1][idx2]
   l.append(d)
print(l)