# Create a class Complex Number with data members as real and imag and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag=imag
    
    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __add__(self,c2):
        c3 = Complex()
        c3.real = self.real +c2.real
        c3.imag= self.imag +c2.imag
        return c3
    
    def __sub__(self,s2):
        s3 = Complex()
        s3.real = self.real - s2.real
        s3.imag= self.imag - s2.imag
        return s3
    
    def __del__(self):
        print(f"release the resources {self.real}")
        
c1 = Complex(5,7)
c2 = Complex(3,4)
print(c1)
print(c2)
c3 = c1 + c2
# c1.__add__(c2)
print(c3)
s1 = Complex(4,6)
s2 = Complex(2,4)
print(s1)
print(s2)
s3 = s1 - s2
print(s3)



