#4. Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
#Expected output:
#tuple1 = (99, 88)
#tuple2 = (11, 22)
tuple1,tuple2=tuple2,tuple1
print(tuple1,tuple2)