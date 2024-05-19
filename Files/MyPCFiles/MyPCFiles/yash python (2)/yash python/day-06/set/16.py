#16. Write a Python program to check if a given value is present in a set or not.
s1={1,2,3,4,5,6,7,8}
x=int(input("enter no to be search: "))
if x in s1:
 print(f"{x} exist in set")
else:
 print(f"{x} not exist in set")
