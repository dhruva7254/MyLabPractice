#29. Write a Python program to convert a given tuple of positive integers into an integer.
#Original tuple:
#(1, 2, 3)
#Convert the said tuple of positive integers into an integer:
#123
#Original tuple:
#(10, 20, 40, 5, 70)
#Convert the said tuple of positive integers into an integer:
#102040570
n=int(input("enter size of tupple: "))
t=()
for idx in range(n):
    e=int(input(f"enter element{idx+1} tupple: "))
    t=t+(e,)
print(t)    
s=""
for e in t:
   s=s+str(e)
print(int(s))   
