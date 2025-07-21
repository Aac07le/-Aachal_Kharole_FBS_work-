# WAP to accept basic salary of n employees (n shouls be accepted from user). If salary is below 20000 the , da=10% ,
# ta=12% ,hra=15%  Otherwise da= 15%, ta = 18% , hra = 20%.
# based on this calculate the total salary of each employees and total salary of each employee.
            
            
num = int(input("Enter the number of employees: "))

for i in range(1, num + 1):
    basic_salary = int(input(f"Enter the basic salary of employee {i}: "))

    if basic_salary < 20000:
        da = (basic_salary * 10) / 100
        ta = (basic_salary * 12) / 100
        hra = (basic_salary * 15) / 100
    else:
        da = basic_salary * 0.15
        ta = basic_salary * 0.18
        hra = basic_salary * 0.20

    total_salary = basic_salary + da + ta + hra
    print(f"Total salary of employee {i} is: {total_salary}")
    
    
