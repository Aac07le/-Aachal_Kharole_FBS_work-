# Create a class Distance with data members as km,m and cm and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator 

class Distance:
    def __init__(self,km=0 ,m=0 ,cm = 0):
        self.km = km
        self.m = m
        self.cm = cm
        
    def __del__(self):
        print(f"release resourc {self.km}")
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    def normalize(self): 
        self.m += self.cm // 100
        self.cm = self.cm % 100
        self.km += self.m // 1000
        self.m = self.m % 1000

    def __add__(self, other):
        d3 = Distance()
        self.km + other.km,
        self.m + other.m,
        self.cm + other.cm
    
        d3.normalize()
        return d3

    def __sub__(self, other):
       
        total_cm1 = self.km * 100000 + self.m * 100 + self.cm
        total_cm2 = other.km * 100000 + other.m * 100 + other.cm

        diff_cm = abs(total_cm1 - total_cm2) 
        d3 = Distance()
        diff_cm // 100000
        diff_cm % 100000 // 100
        diff_cm % 100
        return d3

d1 = Distance(5, 60, 125)
d2 = Distance(6, 75, 165)
d3 = d1 + d2
print("Addition:", d3)

d4 = d2 - d1
print("Subtraction:", d4)    
    
        
        
        