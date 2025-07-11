
# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter The Three Digit Number: "))

temp = num

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10

revers = (a * 100) + (b * 10)+ c

if temp == revers:
    print("Given Number is Palindrome: ")
    
else:
    print("Given Number is Not Palindrome: ")