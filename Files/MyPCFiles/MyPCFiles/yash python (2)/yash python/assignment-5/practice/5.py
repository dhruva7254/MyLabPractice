#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
#Sample String : 'Hello', 'World'
#Expected Result : 'Wollo Herld'
#Test cases:
#a. both empty string input b. 'a' , 'abc' c. '' 'abc' d. '123' 'wow'
s1=input("enter string 1: ")
s2=input("enter string 2: ")
s=s2[0:2]+s1[2:len(s1)]+" "+s1[0:2]+s2[2:len(s2)]
print(s)