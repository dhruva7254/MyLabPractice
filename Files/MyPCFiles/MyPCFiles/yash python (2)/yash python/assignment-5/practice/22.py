#22.Write a Python program to sort a string lexicographically.(do both using library and without library)
s=input("enter string for sorting: ")
l=sorted(list(s),key=lambda x:x,reverse=False)
print("".join(l))