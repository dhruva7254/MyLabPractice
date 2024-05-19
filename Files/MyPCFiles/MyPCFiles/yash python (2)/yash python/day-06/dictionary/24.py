#24. Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
string='w3resource'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
d={}
for e in string:
 d[e]=string.count(e)
print(d) 