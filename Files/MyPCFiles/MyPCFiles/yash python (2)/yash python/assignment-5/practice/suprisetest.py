s1=input("enter string: ")
#l=["{","}","(",")","[","]","<",">"]
def function1(s:str):
 if (s.count("(")==s.count(")"))&(s.count("{")==s.count("}"))&(s.count("[")==s.count("]"))&(s.count("<")==s.count(">")):
     print("No error found")
 if (s.count("(")>s.count(")"))|(s.count("{")>s.count("}"))|(s.count("[")>s.count("]"))|(s.count("<")>s.count(">")):
     print("right bracket is missing")
 if (s.count("(")<s.count(")"))|(s.count("{")<s.count("}"))|(s.count("[")<s.count("]"))|(s.count("<")<s.count(">")):
     print("left bracket is missing")
function1(s1)   
s2="{k+1"
print(s2.count("{"),s2.count("("))