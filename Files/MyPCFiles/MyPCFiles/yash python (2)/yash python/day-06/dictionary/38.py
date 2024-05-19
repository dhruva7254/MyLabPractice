#38. Write a Python program to match key values in two dictionaries.
d1={'key1': 1, 'key2': 3, 'key3': 2}
d2={'key1': 1, 'key2': 2,'key3': 2}
#Expected output: key1: 1 is present in both x and y
for key1 in d1:
    for key2 in d2:
        if (key1==key2)&(d1[key1]==d2[key2]):
            print(f"{key1}:{d1[key1]} is presented in both")