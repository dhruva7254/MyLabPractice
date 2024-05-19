s=input("enter string: ")
for idx in range(1,len(s)):
    if s[idx]==s[0]:
        s[idx]='$'
print(s)
