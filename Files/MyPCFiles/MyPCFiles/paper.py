

# #Q 2


# d={'v':[1,4,6,10],'vi':[1,4,12],'vii':[1,3,8]}
# count=0
# for k in d.keys():
#     count=count+1
# print("total keys",count)


# a=input("enter the key")
# for k,v in d.items():
#     if(k==a):
#         print("Value of key :",v)
    


# for v in d.values():
#     for i in v:
#         if(i%2!=0):
#             v.remove(i)
        
# print("Even no:",d)

################################################################################################################
#Q1
def action(l):
  print(l)

  if(len(l)==0):
    print("empty")
  else:
    print("nonempty")
  
  for i in l:
    l.sort()
  
  print(l)


l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
action(l)

############################################################################################################

#Q3
# class centroid:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
       

#     def __print__(self,x,y):
#         print("x=",self.x)
#         print("y=",self.y)

#     def __add__(self,other):
#         x=int((self.x + other.x)/2)
#         y=int((self.y + other.y)/2)
#         return centroid(x,y)
    
#     def __sub__(self,other):
#         x=int(abs((self.x - other.x)/2))
#         y=int(abs((self.y - other.y)/2))
#         return centroid(x,y)


# c1=centroid(10,20)
# c2=centroid(30,40)

# print(c1)
# # e=c1+c2
# # print(e.x,e.y)

# # f=c1-c2
# # print(f.x,f.y)


#################################################################################################