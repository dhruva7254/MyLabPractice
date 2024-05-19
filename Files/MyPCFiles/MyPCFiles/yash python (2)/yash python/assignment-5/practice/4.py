#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
#Sample String : 'ababab'
#Expected Result : 'ab$b$b'
s=input("enter string: ")
s1=s[1:len(s)]
s1=s1.replace(s[0],"$",s1.count(s[0]))
print(s[0]+s1)

