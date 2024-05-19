#30. Write a Python program to remove all duplicates from a given list of strings and return a list 
#of unique strings. Use the Python set data type.
l=["abc","dcf","abc","dcf","asd","aasd","cab","aasd"]
l=list(set(l))
print(l)