#21. Write a Python program to replace the last value of tuples in a list.
l1=[(10, 20, 40), (40, 50, 60), (70, 80, 90),(70, 80)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
x=int(input("enter new last value: "))
t=()
for idx in range(0,len(l1[len(l1)-1])-1):
  t=t+(l1[len(l1)-1][idx],)
t=t+(x,)
l1[len(l1)-1]=t
print(l1)

