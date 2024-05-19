#23. Write a Python program to combine values in a list of dictionaries.
data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#Expected Output: Counter({'item1': 1150, 'item2': 300})
d={}
for e in data:
    d[list(e.values())[0]]=list(e.values())[1]
print(d)
