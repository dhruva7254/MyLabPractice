#17. Write a Python program to check if two given sets have no elements in common.
s1={1,2,3,4}
s2={1,6,-1}
if s1&s2==set():
    print("given set have nothing in comman")
else:
    print(f"given set have {s1&s2} in comman")
