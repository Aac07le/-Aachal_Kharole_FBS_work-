# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter any number:"))

for num in range(1,num+1):
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
    print("Yes, The Given Number is Armstrong NUmber: ")
else:
    print("NOT, The Given Number is not Armstron Number: ")

