class parent:
    n=6
    def __init__(self):
        self.n1=2
        self.n2=3
    def addition(self):
        print(self.n1+self.n2)
    def subtraction(self):
        print(self.n1-self.n2)
    def __add__(self,other):
        print(self.n1*other.n1)
class child(parent):
    def __init__(self,n3:int):
        super().__init__()
        self.n3=n3
    def multiplication(self):
        print(self.n1*self.n2)      
    def devision(self):
        print(self.n1/self.n2)  
    def subtraction(self):
        super().subtraction()
        print(abs(self.n1-self.n2))
    def multiplication_of3(self):
        print(self.n1*self.n2*self.n3)     

c=child(3)
#c.multiplication()
c.subtraction()
#c.multiplication()
#print(c.n)
#c.addition()
#parent().__add__(6)