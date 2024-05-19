#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
  n1=float(input("enter no:"))
except ValueError:
  print("only numeric data allowed")
except:
  print("unidentifed error")
else:
  print("it numeric")    