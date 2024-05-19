class grandfather:
    def __init__(self):
        self.n1=2
        self.n2=6
    def __mul__(self,other):
        print(self.n1*other)
    def multiplication(self):
        print(self.n1+self.n2)
class father(grandfather):
    def __init__(self):
        self.n1=10
    def displayfather(self):
        print("father")
class child(father):
    def __init__(self):
        grandfather.__init__(self)
        super().__init__()
        self.n=6
    def diplaychild(self):
        print("child")
child().__mul__(2)
print(child().n1)
                      
