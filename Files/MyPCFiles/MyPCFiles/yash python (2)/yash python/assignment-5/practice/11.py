#11. Write a Python program to remove characters that have odd index values in a given string.
s=input("enter string: ")
s1=""
for idx in range(len(s)):
    if idx%2==0:
        s1=s1+s[idx]
s=s1
del s1
print(s)        