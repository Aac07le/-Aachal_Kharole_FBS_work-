# Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms.

def fibonacciSeries(num):
    # num = int(input("Enter The Number: "))
    a = 1
    b = 0
    for i in range(1,num+1):
        c = a + b
        print(c)
        a = b
        b = c
num = int(input("Enter The Number: "))
fibonacciSeries(num)