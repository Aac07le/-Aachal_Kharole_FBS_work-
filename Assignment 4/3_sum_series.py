
# WAP to print sum of series upto n
n  = int(input("Enter the valu for n: "))

print("Sum of series: ")

sum = 0
for i in range(1, n + 1):
 sum = sum + i
 print(sum)