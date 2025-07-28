# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = int(input("Enter The Valu For a:"))
sum = 0
i = 0
for i in range(1, 10+1):
    sum += (a ** i) / 1
print(f"sum of series:",sum)


# while i <= 10:
#     sum += (a ** i) / 1
#     i += 1
# print(sum)


