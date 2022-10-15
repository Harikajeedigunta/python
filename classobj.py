class Student:
    group="Aditya"
    def __init__(self,rollno,branch,college):#this
        self.rollno=rollno
        self.branch=branch
        self.college=college
        self.group="aditya"
    def display(self):
        print(self.rollno,self.branch,self.college)
        print(Student.group)
    @staticmethod
    def even(num):
        if num%2:
            print("odd")
        else:
            print("even")
        
s1=Student(123,"cse","AEC")
s1.display()
s1.even(s1.rollno)

#"instance"
#"class"
#"static"
