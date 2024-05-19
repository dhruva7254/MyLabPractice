s=input("enter equation: ")
l=[]
for e in s:
 if (e=="(")|(e==")")|(e=="[")|(e=="]")|(e=="{")|(e=="}")|(e=="<")|(e==">"):
     l.append(e)
print(l)
if len(l)%2!=0:
   print("equation is not valid")
else:
   c=0
   for idx in range(0,len(l)//2):
       print(l[idx]+l[len(l)-1-idx])
       if ((l[idx]+l[len(l)-1-idx])=="()")|((l[idx]+l[len(l)-1-idx])=="{}")|((l[idx]+l[len(l)-1-idx])=="[]")|((l[idx]+l[len(l)-1-idx])=="<>"):
          c=c+1
       else:
          print("equation is not valid")
          break
   if c==len(l)//2:
      print("equation is valid")