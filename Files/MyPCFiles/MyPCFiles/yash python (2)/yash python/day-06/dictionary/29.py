#29. Write a Python program to remove spaces from dictionary keys.
#After removing spaces if keys repeat then keep the latest value.
#Ex. 
#i/p
d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English'], 'S 3':['Math', 'English'], 'S3':['English'], }
#o/p
#{'S001': ['Math', 'Science'], 'S002': ['Math', 'English'], 'S3':['English']}
d1={}
for key in d:
 l1=key.split(" ")
 s=""
 for e in l1:
    if e!='':
        s=s+e
 print(s)  
 d1[s]=d[key]    
print(d1)   