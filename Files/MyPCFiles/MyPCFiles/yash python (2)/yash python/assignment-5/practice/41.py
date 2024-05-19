#41. Write a Python program to strip a set of characters from a string.
#(do both using library and without library)
n=int(input("enter size of set: "))
sc=set()
for idx in range(0,n):
   e=input(f"enter character {idx+1}:")
   sc.add(e)
print(sc)    
s=input("enter string: ")
l=list(s)
for e in l:
    if e in sc:
        l.remove(e)
print("".join(l))        
