#30. Write a Python program to get the top three items in a shop.
d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#Expected Output:
#item4 55
#item1 45.5
#item3 41.3
d1=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
lk=list(d1.keys())
lv=list(d1.values())
for a in range(0,3):
    print(lk[a],lv[a])