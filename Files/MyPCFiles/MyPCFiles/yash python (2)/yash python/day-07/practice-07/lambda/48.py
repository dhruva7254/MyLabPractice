#48. Write a Python program to sort a given list of strings (numbers) numerically using lambda.
#Original list:
l=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
#Sort the said list of strings(numbers) numerically:
#['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
print(sorted(l,key=lambda x:int(x),reverse=False))