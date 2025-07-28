# Write a program to check if entered number is a palindrome or not.
def palindrome(num):
   
    a = num % 10
    num = num // 10
    b = num % 10
    c = num // 10
    
    reverse = (a * 100) + (b * 10) + c
    return reverse
    
num = int(input("Enter The Any Number: "))
ans = palindrome(num)
if ans == num:
    print(f"Yes!!, The Given Number {num} Is Pallindrome: {ans} ")
else:
    print(f"NO !!, The Given Number {num} Is Not Palindrome: {ans}")
