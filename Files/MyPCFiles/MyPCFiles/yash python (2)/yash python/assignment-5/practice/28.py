#28. Write a Python program to add prefix text to all of the lines in a string.(do both using library and without library)
#Example:
#Add prefix "line1:" to every line in question 26
s="Nature around us is a gift. We need to handle it wisely.Nature's gifts are for everyone and many generations. Every generation,need to think before making a damage to these gifts."
w=int(input("enter width of statment: "))
for n in range(0,(len(s)//w)+1):
  print(F"Line{n+1}:{s[0:w-1]}")
  s=s[w-1:(len(s)+1)]