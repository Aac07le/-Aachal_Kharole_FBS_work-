# Write a program to calculate area of rectangle.
def Area():
    length = int(input("Enter The Length OF Rectangle: "))
    breadth = int(input("Enter The Breadth Of Rectangle"))
    Area = length * breadth
    return Area
ans = Area()
print(ans)