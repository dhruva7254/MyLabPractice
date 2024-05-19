#43. Write a Python program to convert more than one list to a nested dictionary.
#Original strings:
l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3=[85, 98, 89, 92]
#Nested dictionary:
#[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
l4=[]
l5=[]
l6=[]
for e in dict(zip(l2,l3)).items():
     l4.append(e)
     l5.append(dict(l4))
     l4=[]
for e1 in dict(zip(l1,l5)).items():
     l4.append(e1)
     l6.append(dict(l4))
     l4=[]
print(l6)     
     
