#46. Write a Python program to find the index position and value of the maximum and minimum values in a given list of numbers using lambda.
#Original list:
l=[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
#Index position and value of the maximum value of the said list:
#(5, 89)
#Index position and value of the minimum value of the said list:
#(3, 10.11)
fmax=lambda x:max(x)
fmin=lambda x:min(x)
print(f"Index position and value of the maximum value of the said list:{(l.index(fmax(l)),fmax(l))}")
print(f"Index position and value of the minimum value of the said list:{(l.index(fmin(l)),fmin(l))}")