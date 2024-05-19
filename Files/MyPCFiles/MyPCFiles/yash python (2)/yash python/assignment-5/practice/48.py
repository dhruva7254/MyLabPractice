#48. Write a Python program to swap commas and dots in a string.
#Sample string: "32.054,23"
#Expected Output: "32,054.23"
s=input("enter string: ")
l=list(s)
l1=[]
for idx in range(0,len(l)):
    if l[idx]==".":
        l[idx]=","
        l1.append(idx)
    if (idx not in l1)&(l[idx]==","):
        l[idx]="."
print("".join(l))