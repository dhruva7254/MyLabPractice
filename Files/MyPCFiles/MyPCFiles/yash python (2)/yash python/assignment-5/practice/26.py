#26. Write a Python program to display formatted text (width=50) as output.
#a. using library (hint. textwrap)
#b. without using any library
#Sample input
s="Nature around us is a gift. We need to handle it wisely.Nature's gifts are for everyone and many generations. Every generation,need to think before making a damage to these gifts."
w=50
#output:(-> and <- arrow are shown to highlight start and end of line)
#->Nature around us is a gift. We need to handle it <-
#->wisely.Nature's gifts are for everyone and many g<-
#->enerations. Every generation,need to think before<-
#-> making a damage to these gifts.
for n in range(0,(len(s)//w)+1):
  print("->",s[0:w-1],"<-")
  s=s[w-1:(len(s)+1)]


