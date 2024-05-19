#38. Write a Python program to count occurrences of a substring in a string.
#(do both using library and without library)
s= input("input string: ")
sb= input("input sub_string: ")
c=0
if sb!="":
 for idx in range(0,len(s)):
    if s[idx:(idx+len(sb))]==sb:
        c=c+1
 print(c)        
else:
 print(0)    
