# write a function
# take string input
# check right format 
# check open and close matching brackets 
# - no error found
# - right side bracket missing
# - left side bracket missing
# - "(2+3}-{4+5)"

def cherigfor(str s):
    a = "{(23/2)+(34+22}/2"
    lc1 = 0
    lc2 = 0
    lc3 = 0
    for i in a:
        if i == '{'
            lc1 += 1
        if i == '('
            lc2 += 1
        if i == '['
            lc3 += 1
        if i == '<'
            lc4 += 1


    return a
s=input("input mathematical expression: ")
n=cherigfor(s)
print(n)
