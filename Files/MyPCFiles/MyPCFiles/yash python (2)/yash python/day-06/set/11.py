#11. Write a Python program to create a shallow copy of sets.
#Note : Shallow copy is a bit-wise copy of an object. 
#A new object is created that has an exact copy of the values in the original object.
s1={1,2,3,4,5,6,7,8}
s2=s1.copy()
print(id(s2),id(s1))