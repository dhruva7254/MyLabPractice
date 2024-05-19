#12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#Original arrays:
l=[-1, 2, -3, 5, 7, 8, 9, -10]
#Rearrange positive and negative numbers of the said array:
#[2, 5, 7, 8, 9, -10, -3, -1]
l2=sorted(filter(lambda x:x>=0,l),key=lambda x:x,reverse=False)+sorted(filter(lambda x:x<0,l),key=lambda x:x,reverse=False)
print(l2)

