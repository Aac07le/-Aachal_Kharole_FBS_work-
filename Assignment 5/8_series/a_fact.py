# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter the value for series n: "))

final_fact = 0

for i in range(n, 0, -1):
    
    
    fact = 1
    for j in range(2, i+1):
        fact = fact * j
        
    print(f"Factorial of {i} is {fact}.")

    final_fact += fact

print(f"Factorial of given series: {final_fact}")



