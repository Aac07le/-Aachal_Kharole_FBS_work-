# Write a program to find sum of digits using recursion.
def sumOfDigit(num):
    if num == 0:
        return 0
    
    else:
        a = num  % 10
    return a + sumOfDigit(num // 10) 


num = int(input("Enter the digit: "))
ans = sumOfDigit(num)
print(ans)