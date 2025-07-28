# Sum of all prime numbers between 1 to n.
def prime(n):
    sum = 0
    for num  in range(2,n+1):
        for j in range(2,num):
            if ( num % j == 0):
                break
        else:
            sum = sum + num
            
    return sum
            
n = int(input("Enter The Valu For n: "))
ans = prime(n)
print(ans)