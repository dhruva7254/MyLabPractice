def mingam(stg):
    ks = 0
    ss = 0
    v = 'AEIOU'
    for i in range(len(stg)):
        if stg[i] in v:
            ks += (len(stg)-i)
        else:
            ss += (len(stg)-i)
    if ks > ss:
        print("kevin",ks)
    elif ks < ss:
        print("stuart",ss)
    else:
        print("draw")
s = input("Enter the String: ")
mingam(s)