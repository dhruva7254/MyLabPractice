#10. Write a Python program to compute the square of the first N Fibonacci numbers, 
#using the map function and generate a list of the numbers.
n=int(input("enter no of terms: "))
l1=[0,1]
#for idx in range(2,n):
#    l.append(l[idx-1]+l[idx-2])
#print(l)    
l2=list(map(lambda x:l1.append(l1[x-1]+l1[x-2]),list(range(2,n))))
print(l1)
l2=list(map(lambda x:x**2,l1))
print(l2)
