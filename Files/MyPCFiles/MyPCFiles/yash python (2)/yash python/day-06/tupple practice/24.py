#24. Write a Python program to count the elements in a list until an element is a tuple.
l1=[1,2,3,4,('item3', '24.5'),2,('item3', '24.5')]
for idx in range(0,len(l1)):
   if type(l1[idx])==tuple:
      break
print(idx)



