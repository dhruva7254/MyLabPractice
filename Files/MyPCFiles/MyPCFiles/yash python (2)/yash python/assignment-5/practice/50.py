#50. Write a Python program to split a string on the last occurrence of the delimiter.
s=input("enter string: ")
idx=s.rindex(",")
l=[s[0:idx+1],s[idx+1:len(s)]]
print(l)