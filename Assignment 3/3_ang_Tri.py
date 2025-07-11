# Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = float(input("Enter The First Angle of Triangle:" ))
angle2 = float(input("Enter The Second Angle of Triangle: "))
angle3 = float(input("Enter The Third Angle of Triangle: "))

sum_of_angle = angle1 + angle2 + angle3

if(sum_of_angle == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0):
    print("Triangle Is valid: ")
else:
    print("Triangle Is Not Valid: ") 