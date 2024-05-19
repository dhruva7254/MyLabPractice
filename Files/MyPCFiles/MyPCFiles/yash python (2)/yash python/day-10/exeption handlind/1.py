#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
  n1=int(input("enter no:"))
  n2=int(input("enter no:"))
  a=n1/n2
except ValueError:
  print("enter integer as input:")
except ZeroDivisionError:
  print("second integer should be  non-zero: ")
except:
  print("unidentified error")
else:
  print(a)