#28. Write a Python program to convert a tuple of string values to a tuple of integer values.
#Original tuple values:
t=(('333', '33'), ('1416', '55'))
#New tuple values:
#((333, 33), (1416, 55))
t1=()
for e in t:
    t2=()
    for e1 in e:
        e1=int(e1)
        t2=t2+(e1,)
    t1=t1+(t2,)
print(t1)    