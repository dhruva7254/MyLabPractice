#31. Write a Python program to compute the element-wise sum of given tuples.
#Original tuples:
t1=(1, 2, 3, 4)
t2=(3, 5, 2)
t3=(2, 2, 3, 1)
#Element-wise sum of the said tuples:
#(6, 9, 8, 6)
t=()
if len(t1)==min([len(t1),len(t2),len(t3)]):
   for idx in range(len(t1)):
      t=t+((t1[idx]+t2[idx]+t3[idx]),)  
   print(t)
elif len(t2)==min([len(t1),len(t2),len(t3)]):
   for idx in range(len(t2)):
      t=t+((t1[idx]+t2[idx]+t3[idx]),)  
   print(t)
elif len(t3)==min([len(t1),len(t2),len(t3)]):
   for idx in range(len(t3)):
      t=t+((t1[idx]+t2[idx]+t3[idx]),)  
   print(t)