def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for x in range(start,end+1):
 output = factorial(x)
    
 print(f"Factorial of {x} is {output}")

