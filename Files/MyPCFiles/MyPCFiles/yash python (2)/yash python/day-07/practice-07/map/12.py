#12. Write a Python program to find the ratio of positive numbers, negative numbers and zeroes in an array of integers.
l=[0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
lp=list(filter(lambda x:x<0,l))
ln=list(filter(lambda x:x<0,l))
