#45. Write a Python program to convert string elements to integers inside a given tuple using lambda.
#Original tuple values:
t=(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
#New tuple values:
#((233, 33), (1416, 55), (2345, 34))
t1=tuple(map(lambda x:(tuple(filter(lambda x1:x1.isnumeric(),x))),t))
print(t1)
t2=tuple(map(lambda x:(tuple(map(lambda x1:int(x1),x))),t1))
print(t2)