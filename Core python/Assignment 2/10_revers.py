
# Write a program to reverse three-digit number.

num = int(input("Enter three digit number: "))

a = num % 10
num = num // 10
b = num % 10
num = num // 10

reverse = (a * 10)+ b
c = num % 10
num = num // 10
reverse = (b * 10) + c

print("reverse valu is: ", a, b, c)

# print("reverse valu is: ", b)
# print("reverse valu is: ", c)