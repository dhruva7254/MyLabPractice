#42. Write a Python program to filter a dictionary based on values.
#Original Dictionary:
d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
#Marks greater than 170:
#{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
d1={}
n=int(input("enter no: "))
for key in d:
    if d[key]>n:
        d1[key]=d[key]
print(d1) 
print(dict(filter(lambda x:x[1]>170,d.items())))       
