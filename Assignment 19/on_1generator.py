# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.
             
def fibonacciSeries(num):
    a =0 
    b = -1   
    while a <= num:   
        yield a
        a, b = b, a + b  


num = int(input("Enter the value: "))
result = fibonacciSeries(num)
for i in result:
    print(i, end=" ")
    
 

