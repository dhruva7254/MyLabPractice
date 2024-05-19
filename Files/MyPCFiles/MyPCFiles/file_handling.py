f=open("sample_file.txt")
print(f.read())
f.close()

with open("sample_file.txt") as f:
    print(f.read())
print("outside")
print(f.read())   # ValueError: I/O operation on closed file.

