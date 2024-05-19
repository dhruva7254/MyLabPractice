#24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of 
#numbers. Use the Python set.
s={1,2,-2,3,4,5,6,7,12,11,8,9}
l=list(s)
m=max(l)      
l.remove(m)
n=max(l)
print(m,n)
