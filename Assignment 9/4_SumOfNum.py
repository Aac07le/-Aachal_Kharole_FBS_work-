# Write a program to find sum of n numbers using recursion.

def sumOfNumber(num):
    if num ==0:
        return 0
    else:
     return num + sumOfNumber(num - 1)
num = int(input ("Enter The Valu For num: "))
ans = sumOfNumber(num)
print(ans)