#50. Write a Python program to remove specific words from a given list using lambda.
#Original list:
l=['orange', 'red', 'green', 'blue', 'white', 'black']
#Remove words:
lr=['orange', 'black']
#After removing the specified words from the said list:
#['red', 'green', 'blue', 'white']
lo=list(map(lambda x:l.remove(x),lr))
print(l)

