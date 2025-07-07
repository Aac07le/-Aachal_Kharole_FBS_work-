#  WAP to calculate the total cost of painting . 
# The interior of building with four equal  sized walls.

length = float(input("Enter the Length of wall in meter: "))

hight = float(input("enter the hight of wall in meter: "))

cost_per_sqe_meter = float(input("Enter the cost of painting in per square meter: "))

Total_area = 4 * length * hight

total_cost = Total_area * cost_per_sqe_meter 

print("Total cost of painting is to: ", total_cost)
