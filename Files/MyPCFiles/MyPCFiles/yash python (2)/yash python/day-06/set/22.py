#22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
s={1,2,-2,3,4,5,6,7,12,8,9}
n=int(input("enter no: "))
for e1 in s:
    for e2 in s:
        if (e1!=e2)&(e1+e2==n)&(e1<e2):
            print(e1,e2,sep=":")
