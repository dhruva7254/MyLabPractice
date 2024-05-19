#21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
data={'1':['a','b'], '2':['c','d']}
#Expected Output:
#ac
#ad
#bc
#bd
l=list(data.values())
for idx in range(0,len(l)-1):
    for e1 in l[idx]:
        for e2 in l[idx+1]:
            print(e1+e2)