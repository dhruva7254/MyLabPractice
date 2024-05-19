#9. Write a Python program to remove the nth index character from a nonempty string.
s=input("enter string:")
n=int(input("enter index: "))
s1=s[0:n]+s[n+1:len(s)]
print(s1)