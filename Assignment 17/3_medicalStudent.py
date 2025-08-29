# create a class MedicalStudent inherited from student eith following 
# i] Data members : specilization, ii. MarkOfInternship
# Add Methods:
# i. PArametrized constructor, ii. Display, ii. Accept, iv. override Method CAAlculateRank, Override__str__method.

class Student:
    def __init__(self,stdanme,stdRollNo,percentage):
        self.stdname = stdanme
        self.stdRollNo = stdRollNo
        self.percentage = percentage
            
    def display(self):
        print(f"NAME OF THE STUDENT IS: {self.stdname}")
        print(f"STUDENT ROLLNUMBER IS: {self.stdRollNo}")
        print(f"PERCENTAGE  OF THE STUDENT: {self.percentage}")
        
    def accept(self,stdname,stdRollNo,percentage):
        self.stdname = stdname
        self.stdRollNo = stdRollNo
        self.percentage = percentage
        
    def CalRank(self):
        if self.percentage > 80:
            print("WITH FIRST RANK")  
        elif self.percentage > 60:
            print("PASS WITH GOOD MARKS")  
        else:
            print("NEED TO IMPROVEMENT")
            
    def __str__(self):
        return f"{self.stdname} {self.percentage} {self.stdRollNo}"
        
class MedicalStudent(Student):
    def __init__(self,stdname,stdRollNo,percentage,specialization,MarkOfInternship):
        super().__init__(stdname,stdRollNo,percentage)
        self.specialization = specialization
        self.MarkOfInternship = MarkOfInternship  
        
    def display(self):
        super().display()
        print(f"specialization : {self.specialization}")
        print(f"MARKS OF INTERNSHIP:  {self.MarkOfInternship}")
        
    def Accept(self,stdname,stdRollNo,percentage,specialization,MarkOfInternship):
        self.stdname = stdname
        self.stdRollNo = stdRollNo
        self.percentage = percentage
        self.specialization = specialization
        self.MarkOfInternship = MarkOfInternship
        
    def CalRank(self):
        final_mark = self.percentage + (self.MarkOfInternship * 0.1)
        if final_mark > 85:
            print("WITH DISTINCTION")  
        elif self.percentage > 65:
            print("PASS WITH GOOD MARKS")  
        else:
            print("NEED TO IMPROVE")
            
    def __str__(self):
        return (f"{super().__str__()} |specialization:  {self.specialization}",f"| Internship mark: {self.MarkOfInternship}")
    
n = int(input("ENTER THE PERCENTAGE: "))
intern_mark = int(input("ENTER THE INTERNSHIP MARK: "))         
s1 = MedicalStudent("Aachal", 35, n,"cardiology",intern_mark)  
s1.display()      

s1.CalRank()