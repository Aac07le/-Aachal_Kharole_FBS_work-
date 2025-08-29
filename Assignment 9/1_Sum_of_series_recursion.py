# Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def sum_of_factorials(n):
    if n == 1:
        return 1
    else:
        return factorial(n) + sum_of_factorials(n - 1)

n = int(input("Enter the value of n: "))
result = sum_of_factorials(n)

print(f"Sum of series 1! + 2! + 3! + ... + {n}! is: {result}")