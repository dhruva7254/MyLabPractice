#39. Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda.
#Original list:
l=['red', 'black', 'white', 'green', 'orange']
#Substring to search:
#ack
#Elements of the said list that contain specific substring:
#['black']
#Substring to search:
#abc
#Elements of the said list that contain specific substring:
#[]
s=input("enter substring: ")
print(list(filter(lambda x:s in x,l)))