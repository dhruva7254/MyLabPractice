l=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
l1=[l[0]]
for idx in range(1,len(l)):
    if (set(l[0])-set(l[idx]))==0:
        l1.append(l[idx])
print(l1)