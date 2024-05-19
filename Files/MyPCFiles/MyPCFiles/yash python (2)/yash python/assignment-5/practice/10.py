#10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
s=input("enter string: ")
print(s[len(s)-1]+s[1:len(s)-1]+s[0])