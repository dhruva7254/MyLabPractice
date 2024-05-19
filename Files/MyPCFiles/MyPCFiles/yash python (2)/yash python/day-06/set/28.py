#28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, 
#adding up to a target number.
l=[1,2,3,4,5,6,5]
t=int(input("enter target no: "))
s=set()
for e1 in l:
    for e2 in l:
        for e3 in l:
            if (e1<e2<e3)&(e1+e2+e3==t):
                s.add((e1,e2,e3))
print(s)                

