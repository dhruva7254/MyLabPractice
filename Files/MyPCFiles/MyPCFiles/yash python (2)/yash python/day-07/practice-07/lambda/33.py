#33. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
#Input the string: W3resource
#['Valid string.']
s=input("enter string for verification: ")
cl=len(list(filter(lambda x:x.islower(),s)))
cu=len(list(filter(lambda x:x.isupper(),s)))
cn=len(list(filter(lambda x:x.isnumeric(),s)))
if (cl>=1)&(cu>=1)&(cn>=1):
    print("['Valid string.']")
else:
     print("['inValid string.']")  

