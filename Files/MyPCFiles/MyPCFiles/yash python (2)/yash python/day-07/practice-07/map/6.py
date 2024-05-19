#6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. 
#Use the map() function.
l=['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']
s=set(l)
lu=list(map(lambda x:(x.upper(),x.lower()),s))
print(lu)
