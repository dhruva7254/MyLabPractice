#20. Write a Python function to reverse a string if its length is a multiple of 4.
def reversefn(a:str):
    if len(a)%4==0:
        return a[::-1]
    else:
        print("enter string with length of multiple of 4")
a=input("enter string: ")
print(reversefn(a))
