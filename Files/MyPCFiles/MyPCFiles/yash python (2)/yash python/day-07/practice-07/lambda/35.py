#35. Write a Python program to check whether a specified list is sorted or not using lambda.
#Original list:
#l=[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
#Is the said list is sorted!
#True
#Original list:
l=[1, 2, 6, 4, 8, 10, 12, 14, 16, 17]
#Is the said list is sorted!
#False
if l==sorted(l,key=lambda x:x,reverse=False):
    print(True)
else:
    print(False)