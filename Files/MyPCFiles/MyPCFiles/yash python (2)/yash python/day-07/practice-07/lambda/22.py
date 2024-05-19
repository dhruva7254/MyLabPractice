#22. Write a Python program that sums the length of a list of names after removing those that start with lowercase letters. 
#Use the lambda function.
#Result:
#16
l=['Larry', 'curly', 'Moe'," ","Yash"]
s=0
for e in list(filter(lambda X:X[0].isupper(),l)):
      s=s+len(e)
print(s)      
