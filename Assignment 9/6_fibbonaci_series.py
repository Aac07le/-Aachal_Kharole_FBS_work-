# Write a program to print Fibonacci series using recursion.
def fibbonaciSeries(a,b,num):
    if (num > 0):
     c = a + b
     print(c)
     fibbonaciSeries(b,c,num-1)

num = int(input("Enter The valu: "))
fibbonaciSeries(-1,1,num)
