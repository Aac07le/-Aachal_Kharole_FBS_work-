# Write a program to check whether a number is prime or not using recursion.

def is_prime(num, i=2):

    if num <= 1:
        return False
    if i * i > num:
        return True
    if num % i == 0:
        return False 
    
    return is_prime(num, i + 1)

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
