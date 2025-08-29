# Write a program to reverse a number using recursion.

def reverse_number(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverse_number(num // 10, rev * 10 + num % 10)


num = int(input("Enter a number to reverse: "))


if num < 0:
    result = -reverse_number(-num)
else:
    result = reverse_number(num)

print(f"Reversed number is: {result}")