# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

# n = int(input("Enter Number of n:"))
# sum = 0
# for i in range (n):
#     sum += 2 ** i
#     i += 1
# print(sum)

n = int(input("Enter Number of n:"))
sum = 0
i = 0
while i < n:
    sum += 2 ** i
    i += 1
print(sum)