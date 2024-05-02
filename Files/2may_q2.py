response_records = [{'rec1':{'col1':1,'col2':10,"col3":5}},
                    {'rec2':{'col1':2,'col2':60,"col3":67}},
                    {'rec3':{'col1':6,'col2':30,"col3":2}},
                    {'rec4':{'col1':3,'col2':20,"col3":99}},]
# o/p: mean col1 : 3.0 col2 : 30.0 col3 : 43.25
# print(response_records)
# print(response_records[0])
# b=response_records[0]
# print(type(b))
# print(b.keys())
# print(response_records[0].values())
# a=response_records[0].values()
# print(a)
# print(type(a))
# print(response_records[0].keys())

sum=0
for c in response_records:
#    print(c)
    for d in c.values():
#        print(d)
        for e in d.values():
            sum = sum + e
#            print(e)
            # sum += e
            # print(sum)
            break
            #continue
print(sum//4)

#            f=list(e)
#            print(f)
#            f=[]
#            print(f.append(e))

