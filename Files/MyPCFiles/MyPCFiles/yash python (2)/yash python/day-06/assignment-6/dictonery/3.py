#3. Write a menu driven program to practice Dictionary functions.
#Write a program to accept name of a person and their vehicle and store it in a dictionary.
#Ask user if they want to continue to accept multiple values.
#Display following menu:
#a. Add new person name and a vehicle name.
#b. Delete a person name and vehicle name from the dictionary.
#----Accept person name from user.
#----Check whether person name exists in the dictionary.
#----If exists show person name and vehicle name to the user.
#----Confirm for deletion, if user enters y
#then delete otherwise no. Display appropriate message.
#c. Modify vehicle name for the person
#----Accept a person name from user.
#----Check whether the person’s name exists.
#----If the name exists, show the person’s name and vehicle name to user.
#Ask for new value and then overwrite the old value.
#d. Search vehicle for the given person’s name.
#e. Search list of people, who have given a vehicle
#f. Display all person names.
#g. Display all vehicle names.
#h. Exit
n=int(input("enter length of dictonery: "))
d={}
for a in range(1,n+1):
  key=input(f"enter name of person {a} or press q to quit : ")
  value=input(f"enter name of vehicle {a}: ")
  if (key!="q")|(value!="q"):   
     d[key]=value
  else:
     break   
print(d)  
choice=""
while(choice!="h"):
 print("choice menue:","\n","a. Add new person name and a vehicle name.","\n","b. Delete a person name and vehicle name from the dictionary."
      ,"\n","c. Modify vehicle name for the person","\n","d. Search vehicle for the given person’s name.","\n"
      ,"e. Search list of people, who have given a vehicle","\n","f. Display all person names.","\n","g. Display all vehicle names."
      ,"\n","h. Exit")
 print(d)
 choice=input("enter choice: ")
 if choice=="a":
   key=input(f"enter name of person: ")
   value=input(f"enter name of vehicle: ")   
   d[key]=value
 if choice=="b":
   key=input(f"enter name of person: ")
   del d[key]    
 if choice=="c":
   key=input(f"enter name of person to be modify: ")
   value=input(f"enter name of new vehicle: ")   
   d[key]=value
 if choice=="d":
   key=input(f"enter name of person: ")
   print(d[key])
 if choice=="e":
   for key in d:
      if d[key]!='':
         print(key)
 if choice=="f":
   print(d.keys())        
 if choice=="g":
   print(d.values())    


        