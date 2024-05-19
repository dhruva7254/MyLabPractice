#44. Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
#Original Tuple:
t=((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
#Average value of the numbers of the said tuple of tuples:
#(30.5, 34.25, 27.0)
#Original Tuple:
#t=((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#Average value of the numbers of the said tuple of tuples:
#(25.5, -18.0, 3.75)
t1=()
for e in t:
    s=0
    for a in e:
       s=s+a
    t1=t1+(round(s/len(e),2),)   
print(t1)    