#40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
#{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
#15
#25
#35
#x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
#y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
#z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
n=int(input("enter size of dictonery: "))
d={}
for e in range(n):
    key=input(f"enter key for element{e+1}: ")
    nv=int(input(f"enter size of value list: "))
    lv=[]
    for e1 in range(nv):
        a=int(input(f"enter in {key} key value for element{e1+1}: "))
        lv.append(a)
    d[key]=lv
print(d)        
