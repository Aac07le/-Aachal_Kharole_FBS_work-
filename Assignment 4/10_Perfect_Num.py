# WAP to check if given number is Perfect Number.

n = int(input("Enter Any Number: "))
sum_of_divisior = 0


for i in range(1, n):
    if n % i == 0:  
        sum_of_divisior = sum_of_divisior + i
     

if sum_of_divisior == n:
    print(f"Yes, {n} is a PERFECT NUMBER!!!")
else:
    print(f"No, {n} is NOT a PERFECT NUMBER!!!")

    