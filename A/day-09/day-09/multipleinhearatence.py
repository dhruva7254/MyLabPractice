class father:
    n=6
    def __init__(self):
        self.n1=2
        self.n2=3
    def addition(self):
        print(self.n1+self.n2)
    def subtraction(self):
        print(self.n1-self.n2)
class mother:
    n=2
    def __init__(self):
        self.n3=5
        self.n4=6
    def diplayparrent2(self):
        print("I am mother")
    def multiplication(self):
        print(self.n3*self.n4)      
    def devision(self):
        print(self.n3/self.n4)  
    def addition(self):
        print(self.n3+self.n4)
class boy(father,mother):
    def __init__(self,name:str):
        father.__init__(self)
        mother.__init__(self)
        self.name=name
    def diplayclassname(self):
        print(f"I am boy {self.name}")
    def addall(self):
        self.n8=self.n1+self.n2+self.n3+self.n4
        return(self.n8)
    def addition(self):
        father.addition(self)
        mother.addition(self)
        print(self.n1+self.n4)
        
#c=boy("yash")
#c.diplayclassname()
#c.multiplication()
#mother.devision(c)
#c.addition()
#c.subtraction()
#c.diplayparrent2()
#print(boy.mro())
print(boy("yash").addition())