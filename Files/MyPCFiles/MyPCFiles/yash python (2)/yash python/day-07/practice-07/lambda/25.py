#25. Write a Python program to create the next bigger number by rearranging the digits of a given number.
#Original number: 12
#Next bigger number: 21
#Original number: 10
#Next bigger number: False
#Original number: 201
##Next bigger number: 210
#Original number: 102
#Next bigger number: 120
#Original number: 445
#Next bigger number: 454
n=int(input("enter no: "))
s=str(n)
n2=int(s[0:len(s)-2]+s[len(s)-1]+s[len(s)-2])
print(n2)
n1=lambda x:int(str(x)[0:len(str(x))-2]+str(x)[len(str(x))-1]+str(x)[len(str(x))-2])
print(n1(n))