# Write a program to check if given number is Armstrong or not using recursive function.

def countNumber(n):
    count = 0
    if  n == 0:
        return 0
    else:
        a = n % 10 
        count += 1
        return count +  countNumber(n // 10) 
num = int(input("Enter The Any Digit Number: "))
ans = countNumber(num)

def armstrongNumber(num,ans):
    if num == 0:
        return 0
    else:
        a = num % 10
    return (a ** ans ) + armstrongNumber(num // 10, ans)
    
    
# num = int(input("Enter The Valu for num: "))
result = armstrongNumber(num,ans)
if (result == num):
    print(f"Yes!!!, The Given Number {num} Is Armstrong Number")
else:
    print(f"NO!! The Given Number IS {num} Not Armstrong Number")
    
        