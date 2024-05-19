#42. Write a Python program to count repeated characters in a string.
#(do both using set and without set, in both case store in dictionary)
s='thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2
#ss=set(list(s))
d={}
#for e in ss:
#    if s.count(e)>1:
#     d[e]=s.count(e)
#print(d)   
for e in s:
    if s.count(e)>1:
     d[e]=s.count(e)
print(d)   
