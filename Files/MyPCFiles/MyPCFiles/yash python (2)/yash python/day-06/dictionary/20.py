#20. Write a Python program to print all distinct values in a dictionary.
data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
s=set()
for e in data:
    for k in e:
        s.add(e[k])
print(s)        