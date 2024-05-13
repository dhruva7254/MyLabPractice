# 25) print table of any given number 
#     2,4,6,8,10,12,14,16,18,20

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for num in numbers:
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()  # Add an empty line for readability
