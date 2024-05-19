#29. Write a Python program to set the indentation (4 spaces) of the first line, from input string containing a paragraph of text.
#Sample input
para = """Nature around us is a gift. We need to handle it wisely.
Nature's gifts are for everyone and many generations. Every generation,
need to think before making a damage to these gifts."""
l=para.split("\n")
l[0]="    "+l[0]
for e in l:
    print(e)
    