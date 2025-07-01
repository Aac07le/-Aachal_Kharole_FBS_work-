

length = int(input("Enetr the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
radius = int(input("Enter the radius of the semicircle: "))

# area of rectangle (length * breadth)
area_rectangle = length * breadth

# area of semicircle 
area_semicircle = 0.5 * 3.14 * radius * radius

# total area (rectangle + semicircle)
total_area = area_rectangle + area_semicircle

# perimeter = 2 * (length + breadth)
perimeter_rectangle_part  = 2 * length * + 2 * breadth - 2 * radius

# perimeter_semicircle of perimeter
perimeter_semicircle = 3.14 * radius

# total perimeter (rectangle-part + semicircle)
total_perimeter = perimeter_rectangle_part + perimeter_semicircle
                   
print("Area of rectangle: ", area_rectangle) 
print("Area of semicircle: ", area_semicircle)
print("Total area of figure: ", total_area)

print("perimeter of rectangle part: ", perimeter_rectangle_part)     
print("perimeter of semicircle: ", perimeter_semicircle)
print("total perimeter of figure: ", total_perimeter)             
