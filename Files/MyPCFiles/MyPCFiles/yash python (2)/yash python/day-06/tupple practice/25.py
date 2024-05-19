#25. Write a Python program to convert a given string list to a tuple.
string="python 3.0"
#<class 'str'>
#Convert the said string to a tuple:
#('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
#<class 'tuple'>
t=()
for e in string:
    if e!=" ":
       t=t+(e,)
print(t)       
