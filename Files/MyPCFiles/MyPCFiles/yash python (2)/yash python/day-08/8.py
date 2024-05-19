#Q Given list of integers. Use map function to calculate square of all and store in list. 
#Then print sum of all square values.
l=[1,2,3,4,5]
l=list(map(lambda x:x**2,l))
#l=[e**2 for e in l]
s=0
for e in l:
    s=s+e
print(s)    