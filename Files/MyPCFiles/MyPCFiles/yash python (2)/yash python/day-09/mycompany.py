class employee:
    company_name="mycompany"
    def __init__(self,empid:int,name:str,designation:str,salary:int,project_ids_assigned:set,skills:list):
      self.empid=empid
      self.name=name
      self.designation=designation
      self.__salary=salary
      self.project_ids_assigned=project_ids_assigned
      self.skills= skills
    def display_projetids(self):
       print(self.project_ids_assigned)
    def display_identity(self):
       print(self.empid)
    @classmethod
    def display_company_details(cls):
       print(cls.company_name)
    def check_relevant_skill(self,s):
       if s in self.skills:
          print(self.empid,self.name)
       else:
          print(f"do not have {s} skill")   


employee1= employee(1,"yash","data_engineer",1200000,{100,200,300},["linux","cloud","SQL","python"])
employee2= employee(2,"HARSH","data_scientists",1500000,{100,200},["cloud","SQL","machine learning"])
employee3= employee(3,"pranjal","MD",12000000,{100},["linux","cloud","SQL","python"])

employee1.display_identity()
employee2.display_identity()
employee3.display_identity()

employee1.display_projetids()
employee2.display_projetids()
employee3.display_projetids()

employee1.display_company_details()
employee2.display_company_details()
employee3.display_company_details()

employee1.check_relevant_skill("machine learning")
employee2.check_relevant_skill("machine learning")
employee3.check_relevant_skill("machine learning")

print(employee1._employee__salary)
print(employee1.company_name)