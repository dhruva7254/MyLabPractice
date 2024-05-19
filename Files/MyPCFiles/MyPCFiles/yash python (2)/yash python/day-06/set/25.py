#25. Given two sets of numbers, write a Python program to find the missing numbers in the second 
#set as compared to the first and vice versa. Use the Python set.
s1={1,2,3,4,5,11,13,7,8}
s2={1,2,3,4,5,6,7,12,8,9}
print(f"missing no in 2nd as compair to 1st is {s1-s2}")
print(f"missing no in 1nd as compair to 2st is {s2-s1}")
