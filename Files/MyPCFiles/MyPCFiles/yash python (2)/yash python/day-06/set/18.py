#18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
s1={1,2,3,4,5,11,7,8}
s2={1,2,3,4,5,6,7,8,9}
if s2>s1:
    print(f"{s2} is superset of {s1}")
else:
    print(f"{s2} is not superset of {s1}")   