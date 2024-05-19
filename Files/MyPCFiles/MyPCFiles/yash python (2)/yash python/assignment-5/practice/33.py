#33. Write a Python program to print the following integers with zeros to the left 
#of the specified width. If integer with greater width, then display error message.
#a. Use format  
#b. write your logic to perform this task
#Example : width =5
#input     output
#345    	  00345
#56789     56789
#0         00000
#123456    Error
n=input("enter no: ")
w=int(input("enter width: "))
if (w-len(n))>=0:
    for e in range(0,w-len(n)):
        n="0"+n
    print(n)
else:
    print("Error")

