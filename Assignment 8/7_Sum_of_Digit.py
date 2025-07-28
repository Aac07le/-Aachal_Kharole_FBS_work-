# Write a program to find sum of digits of a number.

def sumOfDigit(num):
    a = num % 10
    num = num // 10
    c = num % 10
    d = num// 10
    sum = (a + c + d)
    return sum
num = int(input("Enter The Digit: "))
ans = sumOfDigit(num)
print(ans)