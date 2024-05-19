#52. Write a Python program to print all permutations 
#with a given repetition number of characters of a given string.
from itertools import product
s=input("enter string: ")
n=int(input("enter repetition number of characters: "))
a=list(product(s,repeat=n))
for e in a:
    print("".join(e))

