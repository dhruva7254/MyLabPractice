#4. Write a program to display following menu and do the following:
#a. Add new city and trees commonly found in the city.
#b. Display all cities and the list of trees for all cities.
#c. Display list of trees of a particular city.
#---- Accept a city from user search city and if found display list of trees otherwise
#---- Display message not found
#d. Display cities which have the given tree.
#---- Accept a tree name from user and display all cities in which the tree is found.
#e. Delete city ---- Accept city from user and delete the city if found.
#---- Prompt user before deletion
#f. Modify tree list
#---- Accept city and trees to be added in the city. if city exist add trees at the end of the list
#---- Otherwise add city and list
#g. Exit
choice=""
d={"pune":['A'], "kanpur":['B', 'A'], "raipur":['C', 'A'], "mumbai":['D', 'C', 'A']}
while(choice!="g"):
    print("choice menue","\n","a. Add new city and trees commonly found in the city.","\n","b. Display all cities and the list of trees for all cities.","\n"
          "c. Display list of trees of a particular city.","\n","d. Display cities which have the given tree.","e. Delete city","\n"
          ,"f. Modify tree list","\n","g. Exit")
    print(d)
    choice=input("enter choice: ")
    choice=choice.lower()
    if choice=="a":
        key=input("enter city name: ")
        value=list(input("enter trees list: "))
        d[key]=value
    if choice=="b":
        for key in d:
            print(key,"=",d[key])
    if choice=="c":
         key=input("enter city name: ")
         print(d[key])
    if choice=="d":  
          tree=input("enter tree name: ")
          for key in d:
               if tree in d[key]:
                    print(key)
    if choice=="e":  
         key=input("enter city name to be deleted: ")
         del d[key]
    if choice=="f":      
         key=input("enter city name to be modify: ")
         value=list(input("enter new trees list: "))
         d[key]=value
       