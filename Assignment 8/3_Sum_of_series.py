# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum(n):
    sum = 0
    for i in range(1, n + 1):
     sum = sum + i
    return sum

# 1! + 2! + 3!+....+n!

def factorial(n):
   final_fact = 0

   for i in range(1,n+1):
     fact = 1
     for j in range(2, i+1):
        fact = fact * j  
     print(f"Factorial of {i} is {fact}.")
     final_fact += fact
   return f"Factorial of given series: {final_fact}"
   
def exponent(n):
    sum = 0
    for i in range(1,n +1):
       sum += i ** i
    return sum   
   
n  = int(input("Enter the valu for n: "))
result = sum(n)
print("The Sum Of All N Number is:", result)

n = int(input("Enter the value for series n: "))
result = factorial(n)
print(result) 

n = int(input("Enter The Valu for n: ")) 
ans = exponent(n)
print(ans)