
# Given Input

radius = 20
Length = 50
Breadth = 40
cost_barbed_wire = 35
Round_Wire = 5

# perimeter of half circle
Perimeter_of_half_circle = 3.14 *radius + 2 * radius

#  perimeter of rectangle
Perimeter_of_rectangle = Length + (2 * Breadth)

Total_Perimeter = Perimeter_of_half_circle + Perimeter_of_rectangle

Total_length = Total_Perimeter * Round_Wire

Total_cost_of_fencing = Total_length * cost_barbed_wire

print("Perimeter of half circle is equal to: ", Perimeter_of_half_circle)

print("Perimeter of rectangle is equal to: ", Perimeter_of_rectangle)

print("Total perimeter is: ", Total_Perimeter)

print("Total length is equal to: ", Total_length)

print("Total cost of fencing: ",Total_cost_of_fencing ) 