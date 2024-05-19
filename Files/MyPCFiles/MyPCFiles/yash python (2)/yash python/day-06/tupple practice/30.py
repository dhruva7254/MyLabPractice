#30. Write a Python program to check if a specified element appears in a tuple of tuples.
#Original list:
t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
#Check if White presenet in said tuple of tuples!
#True
##Check if White presenet in said tuple of tuples!
#True
#Check if Olive presenet in said tuple of tuples!
#False
s=input("enter element to be search: ")
count=0
for e in t:
    for e1 in e:
        if e1==s:
          count=count+1   
if count>=1:
   print("true")   
else:          
   print("false")   