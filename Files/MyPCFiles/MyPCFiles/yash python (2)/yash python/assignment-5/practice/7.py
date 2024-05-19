#7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the 
#whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'
s=input("enter string: ")
if "not" in s:
    ap=s.index("poor")
    an=s.index("not")
    if an<ap:
        print(s[0:an]+"poor!")
else:
    ag=s.index("good")
    if 'good' in s:
        print(s[0:ag]+"poor!")


