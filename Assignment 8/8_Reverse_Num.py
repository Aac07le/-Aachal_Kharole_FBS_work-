# Write a program find reverse of a number.

def reverseNum(num):
    a = num % 10
    num = num // 10
    b = num % 10
    reverse = (a * 10) + b
    c = num // 10
    reverse = (reverse * 10) + c 
    return reverse
    
num = int(input("enter The Three Digit Number: "))
ans = reverseNum(num)
print(f"The Reverse Number Of {num} is: {ans}")

    