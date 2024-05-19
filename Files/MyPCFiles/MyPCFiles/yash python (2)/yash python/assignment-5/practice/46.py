#46. Write a Python program to convert a given string into a list of words.
#Sample input: 
s='The quick brown fox jumps over the lazy dog.'
#Sample Output:
#['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
print(s.split(" "))#with using split and below without using split
ls=[]
l=[]
for e in s:
    if e!=" ":
       ls.append(e)
    else:
        l.append("".join(ls))
        ls=[]   
    if e==s[len(s)-1]:
        l.append("".join(ls))
print(l)       