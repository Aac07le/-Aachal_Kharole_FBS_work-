# WAP to input all sides of a triangle and check whether triangle is valid or not.

side1 = float(input("Enter side1 of triangle: "))
side2 = float(input("Enter side2 of Triangle: "))
side3 = float(input("Enter side3 of triangle: "))

if( side1 + side2 > side3) and (side1 + side3 > side1) and (side2 + side3 > side1):
    print("Triangle is valid: ") 
    
else:
    print("Triangle is not valid: ")