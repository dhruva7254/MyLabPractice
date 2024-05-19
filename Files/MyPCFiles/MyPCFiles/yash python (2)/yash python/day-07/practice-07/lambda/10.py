#10. Write a Python program to create Fibonacci series up to n using Lambda.
#Fibonacci series upto 2:
#[0, 1]
#Fibonacci series upto 5:
#[0, 1, 1, 2, 3]
#Fibonacci series upto 6:
#[0, 1, 1, 2, 3, 5]
#Fibonacci series upto 9:
#[0, 1, 1, 2, 3, 5, 8, 13, 21]
n=int(input("enter no of terms in Fibonacci series: "))
l=[0,1]
s=0
a=lambda x:l[x]+l[x-1]
for idx in range(1,n-1):
   s=a(idx)
   l.append(s)
print(l)   
