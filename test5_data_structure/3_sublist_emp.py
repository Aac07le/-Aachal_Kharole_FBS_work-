# A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]

# Write a program to sort the list based on salary.
list1 = [[101,"seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]
length = len(list1)


list1.sort(key=lambda x: x[2])

print("Sorted List based on Salary:")
for emp in list1:
    print(emp)