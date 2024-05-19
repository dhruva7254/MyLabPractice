#12. Write a Python program to count the occurrences of each word in a given sentence.
s=input("enter sentence: ")
l=set(s.split(" "))
l.remove('')
d={}
for e in l:
    d[e]=s.count(e)
print(d)    
