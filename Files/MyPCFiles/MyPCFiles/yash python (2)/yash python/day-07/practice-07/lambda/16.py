#16. Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
#Input number of students: 5
#Name: S ROY
#Grade: 1
#Name: B BOSE
#Grade: 3
#Name: N KAR
#Grade: 2
#Name: C DUTTA
#Grade: 1
#Name: G GHOSH
#Grade: 1
#Names and Grades of all students:
#[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
#Second lowest grade: 2.0
#Names:
#N KAR
l=[]
n=int(input("enter no of students: "))
for e1 in range(n):
    name=input(f"enter name{e1+1}: ")
    marks=int(input(f"enter marks{e1+1}: "))
    l.append([name,marks])
print(l)
l1=sorted(l,key=lambda x:x[1],reverse=False) 
for idx in range(len(l1)):
    if l1[idx][1]!=l1[idx+1][1]:
        print(f"Second lowest grade:{l1[idx+1][1]}")
        print(f"Second lowest grade name:{l1[idx+1][0]}")
        break

