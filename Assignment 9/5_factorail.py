# Write a program to find factorial using recursion.
def factorial(num):
    fact = 1
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
num = int(input("Enter The VAlu For num: "))
ans = factorial(num)
print(ans)