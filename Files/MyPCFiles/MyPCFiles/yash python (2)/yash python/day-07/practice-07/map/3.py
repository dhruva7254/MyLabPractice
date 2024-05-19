#3. Write a Python program to listify the list of given strings individually using Python map.
l=['Red', 'Blue', 'Black', 'White', 'Pink']
l1=list(map(lambda x:list(x),l))
print(l1)
