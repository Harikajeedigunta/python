class Personal:
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
        self.a=20
    def display(self):
        print(self.name,self.phno)
class Student(Personal):
    def __init__(self,rollno,branch,name,phno):
        self.rollno=rollno
        self.branch=branch
        self.a=10
        super().__init__(name,phno)
    def display(self):
        print(self.rollno,self.branch)
        super().display()
class Employee(Personal):
    def __init__(self,empid,salary,name,phno):
        self.empid=empid
        self.salary=salary
        super().__init__(name,phno)
    def display(self):
        print(self.empid,self.salary,self.name,self.phno)
        super().display()
s1=Student(123,"cse","Sudhir",6473215)
s1.display()
e1=Employee(523,50000,"Harika",789654)
e1.display()
print(s1.a)



"""
it will check first subcls ins-var nxt sup cls ins-var nxt sub cls cls-var nxt sup cls cls-var 
"""






