#9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
l=[('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg')
    , ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
#Student name:
#['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton']
#Student name:
#['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998']
#Student weight:
#[35, 37, 39, 35]
ln=list(map(lambda x:x[0],l))
ld=list(map(lambda x:x[1],l))
lw=list(map(lambda x:int(x[2][0:2]),l))
print("Student name:","\n",ln)
print("Student date:","\n",ld)
print("Student weight:","\n",lw)


