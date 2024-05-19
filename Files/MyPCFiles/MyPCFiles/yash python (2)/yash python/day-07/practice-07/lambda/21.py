#21. Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
l=[2, 4, 6, 9, 11]
#Given number: 2
#Result:
#4 8 12 18 22
n=int(input("enter no: "))
l1=list(map(lambda x:x*n,l))
for e in l1:
    print(e,end="  ")