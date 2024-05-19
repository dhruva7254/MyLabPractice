from types import UnionType
from typing import Any


class parent:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __add__(self,other:int):
        self.n1=self.n1+other
        return(self.n1)
    def __or__(self,other:int):
        print(self.n1|other)
class child(parent):
    def __mod__(self,other:int):
        if (self.n1%other==0)&(self.n2%other==0):
            print(f"{other} is comman factor of {self.n1}&{self.n2}")
        else:
            print(f"{other} is not comman factor of {self.n1}&{self.n2}")
    def __add__(self,other:int):
        print(super().__add__(other))
        other=self.n1+self.n2
        return(other)      
#child(2,3).__mod__(1)
print(child(2,3).__add__(2))
#print(child(2,3).n1)