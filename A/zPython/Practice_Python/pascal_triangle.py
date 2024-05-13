r0=[1]
n=5
for row in range(n):
    r=[1]
    for i in range(1,len(r0)):
        r.append(r0[i-1]+r0[i]) #i-1 and i from previous row
    r.append(1)
    print(r)
    r0=r