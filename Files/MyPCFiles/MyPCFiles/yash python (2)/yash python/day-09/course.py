class cource:
    course_creater="CDAC"
    def __init__(self,courseid:int,coursename:str,
                 duration:int,hours:int,contents:list,staff_count:int):
        self.courseid=courseid
        self.coursename=coursename
        self.duration=duration
        self.__hours=hours
        self.contents=contents
        self.staff_count=staff_count
    def display_info(self):
        print(f"courseid:{self.courseid},coursename:{self.coursename}")
    @classmethod
    def display_creater(cls):
       print(f"course_creater:{cls.course_creater}")
    def display_courseofcontent(self,s:str):
        if s in self.contents:
            print(f"course dose contain {s}")
        else:
            print(f"course dose not contain {s}")
#objects
course1=cource(1,"DBDA",6,120,["ML","JAVA","PYTHON","TABLU"],4)            
course2=cource(2,"DAC",6,130,["C++","JAVA",".NET","LINUX"],20)            
course3=cource(3,"DITISS",6,100,["ETHIKAL HAKING","LINUX"],4) 
course1.display_courseofcontent("JAVA")  
course2.display_info()
course2.display_creater()
course1.display_creater()
course3.display_creater()
print(course3.courseid)
print(course1._cource__hours)
