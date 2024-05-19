#21. Write a Python program to find all the unique words and count the frequency of occurrence from a given 
#list of strings. Use Python set data type.
l=["asd","d","asd","a","d","b","e","a","abs"]
print(set(l))
for e in set(l):
    print(e,l.count(e))