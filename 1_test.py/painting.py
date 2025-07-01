
# interior
num_interior_walls = int(input("Enter number of interior walls: "))
area_interior_wall = float(input("Enter area of one interior wall: "))
cost_per_unit_interior = float(input("Enter painting cost per unit area for interior walls: "))

# exterior
num_exterior_walls = int(input("Enter number of exterior walls: "))
area_exterior_wall = float(input("Enter area of one exterior wall: "))
cost_per_unit_exterior = float(input("Enter painting cost per unit area for exterior walls: "))

# total area
total_area_interior = num_interior_walls * area_interior_wall
total_area_exterior = num_exterior_walls * area_exterior_wall

# total cost
total_cost_interior = total_area_interior * cost_per_unit_interior
total_cost_exterior = total_area_exterior * cost_per_unit_exterior

# output
print("Total area of interior walls =", total_area_interior)
print("Total painting cost for interior walls = ₹", total_cost_interior)

print("Total area of exterior walls =", total_area_exterior)
print("Total painting cost for exterior walls = ₹", total_cost_exterior)

print("Total painting cost for both interior and exterior = ₹", total_cost_interior + total_cost_exterior)