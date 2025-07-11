
# WAP to print all odd numbers until n.

n = int(input("Enter Valu for n: "))

print("Odd Number 1 to n: ")

for i in range(1, n + 1):
    if i % 2 != 0:
      print(i) 