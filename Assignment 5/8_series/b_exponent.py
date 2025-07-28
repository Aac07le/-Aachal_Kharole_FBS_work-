# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input("Enter The Number for n:"))
sum = 0
i = 1
for j in range(1,n+1):
    sum = 0
    for i in range(1,n+1):
     sum = n ** i
     i += 1
print(sum)