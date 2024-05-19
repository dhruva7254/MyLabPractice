#5. Take a sentence as input from user. Every word is seperated by space. 
#a. Create a word_count dictionary which will have unique words and their count. 
#b. create suffix_count dictionary which will contain count of words ending with 's', 'es', 'ed', 'y', 'en' , etc.
#c. create dictionary word_length_count which will store length of word and count.
#Ex. 
#input_sent= 'CDAC is in Pune'
#There are 2 words of length 4 and 2 words of length 2 so,
#word_length_count = {2:2, 4:2}
s=input("enter sentance: ")
l=s.split(" ")
choice=""
while(choice!="Ex"):
 print("choice menue:","\n"
      "a. Create a word_count dictionary which will have unique words and their count.","\n" 
      "b. create suffix_count dictionary which will contain count of words ending with 's', 'es', 'ed', 'y', 'en' , etc.","\n"
      "c. create dictionary word_length_count which will store length of word and count.","\n"
      "Ex.for exit")
 choice=input("enter choice: ")
 if choice=="a":
   d1={}
   for key in l:
     d1[key]=l.count(key)
   print(f"d1:{d1}")
 if choice=="b":
   d2={}
   le=["s","es","ed","y","en"]
   for e in le:
     a=len(e)
     count=0
     for e1 in l:
         if e1[len(e1)-a:len(e1)]==e:
             count=count+1
     d2[e]=count         
   print(f"d2:{d2}")       
 if choice=="c":
   d3={}
   for key in l:
     d3[len(key)]=l.count(key)
   print(f"d3:{d3}")






