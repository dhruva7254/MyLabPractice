#8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9
l1=["Evejhj", "Alice", "Bob"]
l=[]
for e in l1:
    l.append(len(e))
idx=l.index(max(l))
print(l1[idx],max(l))    

