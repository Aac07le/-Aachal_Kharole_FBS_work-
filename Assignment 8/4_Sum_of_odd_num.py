# Sum of all odd numbers between 1 to n.

def odd(n):
    sum = 0
    for i in range(2,n + 1):
        for j in range(2,i+1):
            if(i % 2 == 0):
                break
        else:
            sum = sum + i
            
    return sum
            
n = int(input("Enter The valu For n: "))
ans = odd(n)
print(ans)