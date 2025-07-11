# WAP to print Armstrong number within a given range
start = int(input("Enter starting Number: "))
stop = int(input("Enter Nmber for stop : "))

for num in range(start,stop+1):
    temp = num
    sum = 0
    count = 0
    while (temp > 0):
        count += 1
        temp //= 10
    temp = num
    sum = 0
    while temp > 0:
        a = temp % 10
        sum += a ** count
        temp //= 10
        
    if sum == num:
        print(num)






