d=[{"rec1":{"col1":1,"col2":10,"col3":5,}},
   {"rec2":{"col1":2,"col2":60,"col3":0}},
   {"rec3":{"col1":6,"col2":30,"col3":0}},
   {"rec4":{"col1":3,"col2":20,"col3":0}},
   {"rec5":{"col1":3,"col2":20,"col3":0}},
   ]
s1=0
s2=0
s3=0
l=[]
for e in d:
    for k1 in e:
        l=l+list(e[k1].values())
print(l)
for n in range(0,len(e[k1])):
 s=0
 for n1 in range(n,len(l),len(e[k1])):
     s=s+l[n1]
 a=s/len(d) 
 print(f"mean col{n+1}:{a}",end=" ")
  
 
 