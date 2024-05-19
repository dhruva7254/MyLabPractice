#18. Write a Python program to find palindromes in a given list of strings using Lambda.
#Orginal list of strings:
l=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
#List of palindromes:
#['php', 'aaa']
print(list(filter(lambda x:x==x[::-1],l)))