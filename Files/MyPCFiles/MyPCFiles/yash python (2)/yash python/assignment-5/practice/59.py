#59. Write a Python program to find the maximum number of characters in a given string.
s=input("enter string: ")
se=set(list(s))
se.remove(" ")
d={}
for e in se:
   d[e]=s.count(e)
d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
for key in d:
   if d[key]==max(list(d.values())):
      print(f"maximim occuring charater in string is {key}:{d[key]}")
  
