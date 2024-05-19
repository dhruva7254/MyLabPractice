#40. Write a Python program to reverse all words in a string.(do both using slice and without library)
#Ex
#input: "i am feeling great here"
#output:"here great feeling am i"
s=input("enter string: ")
print(" ".join(s.split(" ")[::-1]))
    