
# WAP to print Fibonacci series upto n.

num = int(input("Enter The Valu Of num: "))
print("Fibonacci Series is to: ")

a = -1
b = 1

for i in range(2, num + 1):
    c = a + b
    print(c)
    a = b
    b = c
print("end")