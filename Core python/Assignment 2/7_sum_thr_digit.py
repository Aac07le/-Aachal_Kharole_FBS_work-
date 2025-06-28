
# Find the sum of three-digit number.

num = int(input("Enter the three digit number: "))
a = num % 10
#   b = num // 10
num = num // 10
c = num % 10
d = num // 10
sum = a + c + d

print("sum of three digit number is equal to: ", sum)

