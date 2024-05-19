#35. Write a Python program to display a number with a comma separator. 
#After every thousand there should be comma added.
#(do both using library and without library)
#Ex.
#input      output
#0          0
#-123456    -123,456
#123456789  123,456,789
#9876       9,876
#78         78
n=input("enter no: ")
s=""
for e in range(0,len(n)//3+1):
    s=s+n[-1:-4:-1]+","
    n=n[0:len(n)-3]
print(s)
c=len([e for e in s if e!=","])
if c%3==0:
 print(s[::-1][2:len(s)])
else:
 print(s[::-1][1:len(s)]) 
   