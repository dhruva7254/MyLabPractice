#27. Write a Python program to find all the anagrams in a given list of strings and then group them together. 
#Use the Python data type.
l=["abc","dcf","bca","cfd","asd","aasd","cab","saad"]
d={}
for e1 in l:
    for e2 in l:
        if (e1!=e2)&(len(e1)==len(e2))&(set(e1)-set(e2)==set()):
            d[e1]=e2
print(d)