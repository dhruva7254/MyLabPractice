#22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
d={3:2,2:1,4:2,1:2}
l=sorted(d,key=lambda x:-x)
for idx in range(0,3):
    print(l[idx])
