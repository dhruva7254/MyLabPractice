#26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
#Original Tuple:
#t1=(4, 3, 2, 2, -1, 18)
#Product - multiplying all the numbers of the said tuple: -864
#Original Tuple:
#t2=(2, 4, 8, 8, 3, 2, 9)
#Product - multiplying all the numbers of the said tuple: 27648
n=int(input("enter size of tupple: "))
t=()
for idx in range(n):
  e=int(input(f"enter element{idx+1} of tupple: "))
  t=t+(e,)
print(t)
p=1
for e in t:
  p=p*e
print(p)
