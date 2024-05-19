#24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
#Sample Output:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
n1=int(input("enter lower limit of range: "))
n2=int(input("enter upper limit of range: "))
l=[]
#for e in range(n1,n2+1):
#    l.append(e)
#print(list(filter(lambda x:len(str(x))==1,l)))
#print(list(filter(lambda x:x%int(str(x)[1])==0,l)))
for e in range(n1,n2+1):
    count=0
    for a in range(len(str(e))):
        if int(str(e)[a])!=0:
           if e%int(str(e)[a])==0:
              count=count+1
    if count==len(str(e)):
        l.append(e)
print(l)
#print(bool((str(10)[0]!=0)&(10%int(str(10)[0])==0)))   
#if int(str(10)[1])!=0:
#   if 10%int(str(10)[1])==0:
#       print("ok")
