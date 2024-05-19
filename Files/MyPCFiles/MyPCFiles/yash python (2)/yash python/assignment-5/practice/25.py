#25. Write a Python program to create a Caesar encryption.
#Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, 
#the shift cipher, Caesar's code or Caesar shift, is one of the simplest 
#and most widely known encryption techniques. It is a type of substitution 
#cipher in which each letter in the plaintext is replaced by a letter some 
#fixed number of positions down the alphabet. For example, with a left shift 
#of 3, D would be replaced by A, E would become B, and so on. The method is 
#named after Julius Caesar, who used it in his private correspondence.
s=int(input("enter shift: "))
d=input("enter direction of shift L-Left shift,R-Right shift: ")
s1=input("enter string: ")
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if d=="L":
  l=[]
  for e in s1:
    if e.isalpha():  
     if e.islower():
         idx=a.index(e) 
         l.append(a[idx-s])
     if e.isupper():
         idx=b.index(e)
         l.append(b[idx-s]) 
    else:
       l.append(e)     
  print("".join(l))  
if d=="R":
  l=[]
  for e in s1:
    if e.isalpha():  
     if e.islower():
         idx=a.index(e) 
         if (idx+s)>25:
             idx=abs(((25-idx)+1)-s)
             l.append(a[idx]) 
         else:
          l.append(a[idx+s])
     if e.isupper():
         idx=b.index(e)
         if (idx+s)>25:
             idx=abs(((25-idx)+1)-s)
             l.append(b[idx]) 
         else:
          l.append(b[idx+s]) 
    else:
       l.append(e)     
  print("".join(l))  