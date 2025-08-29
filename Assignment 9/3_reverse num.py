# Write a program to reverse a given number using recursive function.
def reverseNumber(num,reverse):
    if num != 0:
        a = num % 10
        reverse = (reverse * 10) + a
        return reverseNumber(num // 10,reverse)  
    else: 
        return reverse
        
num = int(input("Enter The Valu For num: "))
ans = reverseNumber(num,0)
print(f"The Reverse Number Of {num} is to {ans}")