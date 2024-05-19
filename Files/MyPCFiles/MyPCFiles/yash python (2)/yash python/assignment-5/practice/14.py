#14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
s=input("enter string: ")
a=set(s.split(","))
print(a)
print(",".join(sorted([e for e in a],key=lambda x:x,reverse=False)))