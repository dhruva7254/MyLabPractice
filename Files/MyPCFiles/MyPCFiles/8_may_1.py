# # import math
# # import math
# # print(math.factorial(4))
# # print(math.sin(90))

# import math
# print(math.factorial(5))
# print(math.gcd(12,18))
# print(math.lcm(6,12))
# print(math.perm(456,3))
# print(math.comb(5,3))
# print(math.perm(5,3))
# print(math.sqrt(2))
# print(math.pow(4,2))
# print(math.log10(1))
# var = 20
# if var > 30:
#     print("hi")
# elif var == 20:
#     print("ght")
# else:
#     print("ghj")
# # for
# # for else
# # while
# # while else
# i=3 
# if i < 5:
#     pass
# else:
#     print("greater than 5")
# print(1.5e200 *2.0e210)
# print(1/3)
# print(format(1/3, '.3f'))
# print(format(1/3,'.3f'))
# print(1/3 + 1/3 + 1/3 + 1/3 + 1/3 + 1/3)
# print(6*1/3)
# print(format(22/7,'.5f'))
# print("fgh",format("Hello",'^15'),"ght")
# print("fgh",format("Hello",'#<10'),"ght")
# print(ord('a'))
# print(ord('z'))
# print(ord('\n'))
# print(chr(99))
# print("abc\nbcd")
# print(1,'\n',2)
# print("hello \n\n!!")
# print("This is '\t' means tab")
# print("This","is","different",sep='\t')
# print("This","is","different",sep='#')
# print("This","is","different",sep='\n') 
# print("This","is","different",end='\n')
# print(divmod(101,3))
# print(8 << 1)
# print(8 << 2)
# print(32 >> 2)
# """v1 = int(input("enrer marks: "))
# print(v1)
# v2 = int(input("enrer marks: "))
# print(v2)
# sde = 0
# sde = v1 + v2
# print(sde)"""
# x=10
# y=34.4
# print(x and y)
# print(x or y)
# marks=[56,67,78,39,67]
# for i in marks: 
#     if i<50:
#         print("fail")
#         break
# else:
#     print("All pass")
# for i in range(6):
#     print(i)
# tl = int(input())
# import re
# qwe = "dfg frt gft 9089675432 abf ght tyd fgr 8900670045"
# a = re.search('89',qwe)
# b = re.match('89',qwe)
# c = re.findall('89',qwe)
# print(a)
# print(b)
# print(c)
# print(a.span)
# r0=[1]
# #print(r0)
# n=5
# for row in range(n):
#     r=[1]
# #    print(r)
#     for i in range(1,len(r0)):
#         r.append(r0[i-1]+r0[i]) #i-1 and i from previous row
# #        print(r)
#     r.append(1)
#     print(r)
#     r0=r
# r0=[1]
# n=5
# for i in range(5):
#     r=[1]
#     for i in range(1,len(r0)):
#         r.append(r0[i-1]+r0[i])
#     r.append(1)
#     print(r)
#     r0=r
# user_details={'name':'tanvi','address':'mumbai','age':55}
# match user_details:
# case {'name':n,'age':a} if a > 50:
# print("Important user, ",n)
# case {'address':'pune'}: # all other field are not considered in comparison
# print("User is from pune")
# user = {'name':'tushar','address':'mumbai','age':45}
# match user:
#     case {'name':b,'age':c} if c>40:
#         print("important fgh") 
#     case {'address':'mumbai'}:
#         print("from mumbai")
# __add__(self,other)
"""class student:
    course_name="PGDBDA" # class variable
    # self.v1 = 10 # not allowed!!, self is not accessible outside the methods
    def __init__(self,name,rollno,m1_marks,m2_marks):
        self.name=name #instance variable
        self.rollno=rollno #instance variable
        self.m1_marks=m1_marks #instance variable
        self.m2_marks=m2_marks #instance variable
        student.institute="IACSD" # class variable
    def display_info(self):
        print(self.rollno,self.name)
    def calc_total_marks(self):
        print(self.m1_marks+self.m2_marks)
    def display_capacity(cls):
        cls.student_capacity=60 # class variable
        print(cls.student_capacity)"""
class student:
    course_name="pgdbda"
    def __init__(self,name,rollno,m1_marks,m2_marks):
        self.name=name
        self.rollno=rollno
        self.m1_marks=m1_marks
        self.m2_marks=m2_marks
        student.institute="iacsd"
    def display_info(self):
        print(self.rollno,self.name)
    def calc_total_marks(self):
        print(self.m1_marks+self.m2_marks)
    def display_capacity(cls):
        cls.student_capacity=60
        print(cls.student_capacity)
s1 = student("sdf",567,234,453)
s1.display_info()        
print(student.course_name)
print(s1.m1_marks)
s1.m2_marks=341
print(s1.m2_marks)
class ch_name:
    var1 = 100
    var2 = 89
    def __init__(self):
        self.var1 = 678
cn=ch_name()
print(cn.var1)
print(ch_name.var1)
class my_cla1:
    def __init__(self):
        self.var1 = 12
        self.var2 = 13
cvb = my_cla1()
print(cvb.var1)
cvb.var3=56
print(cvb.var3)
del cvb.var2
#print(cvb.var2)
class Course:
    age_cre_cou="iacsd"
    def __init__(self,cid,cname,dur,tothrs,content,staffct):
        self.cid=cid
        self.cname=cname
        self.dur=dur
        self.tothrs=tothrs
        self.content=content
        self.staffct=staffct
        Course.agency="iacsd"
    def display_info(self):
        print(self.cid,self.cname)
    @classmethod
    def display_agency(cls):
        print(cls.age_cre_cou)
c1 = Course(12,"qwe",23,34,['as','df','rt'],45)
c1.display_info()
c1.display_agency()
print(Course.age_cre_cou)
print(Course.__dict__)
class ht:
    def __init__(self):
        self.var1=23
        self.__hide=12
ht1 = ht()
print(ht1.var1)   
#print(ht1.__hide) 
print(ht1._ht__hide)
ht1._ht__hide=456
print(ht1._ht__hide)
print(ht.__doc__)
class A:
    def __init__(self):
        self.var1=34
    def display(self):
        print(self.var1)
    def display_info(self):
        self.var1+=12
        print(self.var1)
class C(A):
    def __init__(self):
        A.__init__()
        self.c=[1,2,3]
l1=[1,2,3,4,5]
def odd_num(a):
    if a%2 == 0:
        print(False)
    else:
        print(True)
odd_num(5)






































