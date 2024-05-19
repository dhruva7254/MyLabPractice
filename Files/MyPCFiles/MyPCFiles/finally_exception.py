def myfun():
    try:
        print("In try block")
        return 1
    except :
        return 2
    finally:
        return 3

print(myfun()) # 3

def myfun1():
    try:
        print("In try block")
        return 1
    except :
        print("In except")
    finally:
        print("In finally")

print(myfun1()) 
#Output of myfun1 is
# In try block
# In finally