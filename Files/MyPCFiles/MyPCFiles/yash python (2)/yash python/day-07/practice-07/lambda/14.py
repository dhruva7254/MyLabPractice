#14. Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
#Sample Output:
#Monday
#Sunday
l=["Monday","Sunday","sdf","fgrt","jd"]
print(list(filter(lambda x:len(x)==6,l)))