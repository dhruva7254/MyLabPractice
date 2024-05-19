#51. Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
#Original list with tuples:
l=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
#Maximum and minimum values of the said list of tuples:
#(74, 62)
l=sorted(l,key=lambda x:x[1],reverse=False)
print(f"{(l[len(l)-1][1],l[0][1])}")