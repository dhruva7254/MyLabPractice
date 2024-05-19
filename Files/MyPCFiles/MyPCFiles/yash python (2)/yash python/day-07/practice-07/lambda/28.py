#28. Write a Python program to sort a given list of lists by length and value using lambda.
#Original list:
l=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
#Sort the list of lists by length and value:
#[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
l1=sorted(l,key=lambda x:len(x),reverse=False)
def function(x:list):
    s=0
    for e in x:
        s=s+e
    return s    
print(sorted(l1,key=lambda x:x[0],reverse=False))
