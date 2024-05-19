#37. Write a Python program to display a number in left, right, and center aligned 
#with a width of 10.
#(do both using library and without library)
#Left aligned (width 10)   :22                                                                                 
#Right aligned (width 10)  :        22                                                                         
#Center aligned (width 10) 
w=int(input("enter width: "))
n=input("enter no: ")
print(f"Left aligned width {w}: ",n,"."*(w-len(n)),sep="")
print(f"right aligned width {w}: ","."*(w-len(n)),n,sep="")
if (w-len(n))%2==0:
 print(f"center aligned width {w}:","."*((w-len(n))//2),n,"."*((w-len(n))//2),sep="")
else:
 print(f"center aligned width {w}:","."*((w-len(n))//2),n,"."*(((w-len(n))//2)+1),sep="")