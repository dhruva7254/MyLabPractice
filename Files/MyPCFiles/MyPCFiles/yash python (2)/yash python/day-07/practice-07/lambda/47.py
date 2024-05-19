#47. Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
#Original list:
l=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
#Sort the said mixed list of integers and strings:
#[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
l1=sorted(list(filter(lambda x:type(x)==int,l)),key=lambda x:x,reverse=False)
l2=sorted(list(filter(lambda x:type(x)==str,l)),key=lambda x:x,reverse=False)
print(l1+l2)