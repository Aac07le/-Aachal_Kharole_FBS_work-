# creatae a class College which has collection of student . add the following method:
# a. parametrized constructor for number of students.
# b. AddStudents
# c. GetStudent
# d. RemoveStudent
# e. Override__str__method

class Student:
    
    def __init__(self,rNo=0,sname = " ",m1=0,m2=0):
        self.sname = sname
        self.rNo = rNo
        self.m1 = m1
        self.m2 = m2
            
    def __str__(self):
        return f"{self.sname} {self.rNo} {self.m1} {self.m3} {self.m4} {self.m5}"
    
    def calPer(self):
        percentage = (self.m1 + self.m2 ) // 5
        print(f"{self.rNo} got {percentage}")
        
    
class College():
    def __init__(self,clgcode=0,clgName = " "):
        self.clgcode = clgcode
        self.clgName = clgName
        self.Student = []
    
    def AddStudent(self):
        rNo = int(input("ENTER THE ROLL NUMBER OF STUDENT WHICH YOU WANT TO ADD: "))
        sname = input("ENTER THE NAME OF THE NEW STUDENT: ")
        m1 = int(input("ENTER THE MARKS OF STUDENT1: "))
        m2 = int(input("ENTER THE MARKS OF STUDENT2: "))
        
        std = Student(rNo,sname,m1,m2)
        self.Student.append(std)
        
    
            
    def GetStudent(self):
        return f"rNo = {self.clgcode} Name {self.clgName} {self.Student}"
        
        
        
    def RemoveStudent(self):
        RollNo = int(input(" ENTER THE ROLL NUMBER OF THEAT STUDENT WHICH YOU WANT TO REMOVE: "))
        for s in self.Student:
            if (s.rNo == RollNo):
                self.Student.remove(s)
                break
        else:
            print("ROLL NUMBER NOT FOUND")
            
    def __str__(self):
        return f"{self.Student} "
    
    

while (ch != 4):
    print()
    print("1. ADD STUDENT")
    print("2. GET STUDENT")
    print("3. REMOVE STUDENT ")
    print("4. EXIT")
    
    
    ch = int(input("ENTER THE CHOICE:"))
    if (ch == 1):
        college1 = College()
        college1.AddStudent()
    elif(ch == 2):
        college1 = College()
        college1.GetStudent()
    elif(ch==3):
        college1 = College()
        college1.RemoveStudent()
    elif(ch == 4):
        print("EXIT")
    
   
                  
        
        
        
            
    
    
            
        
        
        