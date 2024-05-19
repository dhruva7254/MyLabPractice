#51. Write a Python program to find the first non-repeating character in a given string.
s=input("enter string: ")
for e in s:
    if s.count(e)==1:
        print(e)
        break
    