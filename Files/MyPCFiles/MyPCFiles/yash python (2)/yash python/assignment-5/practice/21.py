#21.Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the 
#first 4 characters.
def function21(a:str):
  if len(a)>=4:  
    c=0
    for idx in range(0,4):
        if a[idx].isupper():
            c=c+1
    if c>=2:
        return a.upper()
    else:
        print("2 in first 4 is not uppercase")
  else:
     print("minimum length is 4")      
a=input("enter string: ")
print(function21(a))     
