#13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
#Original arrays:
l=[1, 2, 3, 5, 7, 8, 9, 10]
#Number of even numbers in the above array: 3
#Number of odd numbers in the above array: 5
print(f"Number of even numbers in the above array: {len(list(filter(lambda x:x%2==0,l)))}")
print(f"Number of odd numbers in the above array: {len(list(filter(lambda x:x%2!=0,l)))}")