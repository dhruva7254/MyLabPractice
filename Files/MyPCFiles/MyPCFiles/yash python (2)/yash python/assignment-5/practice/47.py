#47. Write a Python program to lowercase the first n characters in a string.
s=input("enter string: ")
n=int(input("enter no of characters: "))
s1=s[0:n].lower()+s[n:len(s)]
print(s1)
    