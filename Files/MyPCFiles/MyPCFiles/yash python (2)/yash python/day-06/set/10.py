#10. Write a Python program to check if a set is a subset of another set.
s1={1,2,3,4,5,6,7,8}
s2={1,2,3,4,5,6,7,8,9}
if s2>s1:
    print(f"{s1} is subset of {s2}")
else:
    print(f"{s1} is not subset of {s2}")   