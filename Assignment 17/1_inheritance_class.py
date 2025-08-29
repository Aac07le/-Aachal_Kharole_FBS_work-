# create a class student with followings
#  data member: i] studentid, ii] name , iii] Age, iv]percentage
# Add method : parametrise constructor, display, accept, methodcalculate rank,override stringmethod

class Student:
    def __init__(self,stdid,stdName,stdAge,percentage):
        self.stdid = stdid
        self.stdName = stdName
        self.stdAge = stdAge
        self.percentage = percentage
        
    def display(self):
        print(f"STUDENTID {self.stdid}")
        print(f"STUDENT NAME {self.stdName}")
        print(f"SUDENT AGE {self.stdAge}")
        print(f"PERCENTAGE OF THE STUDENT {self.percentage}")
        
    def Accept(self,stdid,stdName,stdAge,percentage):
        
        self.stdid = stdid
        self.stdName = stdName
        self.stdAge = stdAge
        self.percentage = percentage
      
    def __str__(self):
        return(f"{self.stdid}, {self.stdName},{self.stdAge}, {self.percentage}")
      
        
    def calcARank(self):
        if(self.percentage >= 85):
            print("CONGRATULATIONS YOU GOT FIRST RANK!!!!")
        elif self.percentage >= 60:
            print("YOU ARE PASS WITH GOOD MARKS!!!")
        else:
            print("YOU HAVE IMPROVEs")
            
    
percentage = int(input("ENTER THE PERCENTAGE: "))
std1 = Student(stdid="Aachal@123", stdName="AAchal", stdAge=23,percentage = percentage)
std1.display()
std1.calcARank()
print(std1)

