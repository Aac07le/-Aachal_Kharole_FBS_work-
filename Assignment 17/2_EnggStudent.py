# create a class from student as EnggStudent with DAta Members:
# i] Branch , ii] Internal MArks
# Add Methods: Parameterise Constructor,display,Accept,override methodCalculate,override__str__Method


class Student:
    def __init__(self,sid,sname,percentage):
        self.sid = sid
        self.sname = sname
        self.percentage = percentage
        
        
        
    def display(self):
        print(f"NAME OF THE STUDENT: {self.sname}")
        print(f"PERCENTAGE OF STUDENT: {self.percentage}")
        print(f"ID OF THE STUDENT: {self.sid}")
        
    def Accept(self,sname,percentage,branch):
        self.sname =sname
        self.percentage = percentage
        self.branch = branch
        
    
    def CalRank(self):
        if self.percentage > 80:
            print("FIRST RANK")  
        elif self.percentage > 60:
            print("PASS WITH GOOD MARKS")  
        else:
            print("NEED TO IMPROVEMENT")
            
    def __str__(self):
        return f"{self.sname} {self.percentage} {self.branch}"
        
class EnggStudent(Student):
    def __init__(self,sid,sname,percentage,branch ,Internal_mark):
        super().__init__(sid,sname,percentage)
        self.branch = branch
        self.Internal_mark = Internal_mark
        
           
    def display(self):
        super().display()
        print(f"BRANCH: {self.branch}")
        print(f"INTERNAL MARKS: {self.Internal_mark}")

    def accept(self, sid, sname,  percentage, branch, internal_mark):
        # super().accept(stdid, stdName, stdAge, percentage)
        # self.branch = branch
        # self.internal_mark = internal_mark

        self.sid = sid
        self.sname = sname
        self.percentage = percentage
        self.branch = branch
        self.Internal_mark = internal_mark

    def CalcARank(self):
        total = self.percentage + self.Internal_mark
        if total >= 170:
            return "WITH Distinction: "
        elif total >= 120:
            return "WITH First Class: "
        else:
            return "Pass"
        
    def __str__(self):
        return f"{super().__str__()}, {self.branch}, {self.Internal_mark}"



e1 = EnggStudent("Aachal@123", "Aachal",85,"INFOEMATION TECHNOLOGY", 90)
e1.display()
print("Rank:", e1.CalcARank())
print(e1)
     
        
        
       
        
        
    
        
        
        
    