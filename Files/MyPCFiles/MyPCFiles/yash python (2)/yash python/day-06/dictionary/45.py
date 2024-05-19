#45. Write a Python program to verify that all values in a dictionary are the same.
#Original Dictionary:
d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
#Check all are 12 in the dictionary.
#True
#Check all are 10 in the dictionary.
#False
def function45(d:dict,n:int):
 count=0
 for key in d:
    if d[key]==n:
        count=count+1
 if count==len(d):
     return True  
 else:
     return False      
print(function45(d,12))