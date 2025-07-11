# WAP to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = float(input("Enter first side of Triangle: "))
side2 = float(input("Enter second side of Triangle: "))
side3 = float(input("Enter third side of Triangle: "))

if(side1 + side2 > side3 ) and (side1 + side3 > side2) and (side3 + side2 > side1):
    print("Triangle is valid: ")
    
    if(side1 == side2 == side3):
        print("Triangle is Equilateral: ")
        
    elif(side1 == side2 or side2 == side3 or side1 == side3):
        print("Triangle is Isoscales: ")
        
    else:
        print("Triangle is an Scalene: ")
else:
    print("Triangle is not valid: ")
    