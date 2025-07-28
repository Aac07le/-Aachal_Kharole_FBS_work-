# Write a program to check if entered year is a leap year or not.

def count(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count
    
def Armstrong(num):
    
    digit_count = count(num)
    sum = 0
    while num != 0:
      a = num  % 10
      num = num // 10
      sum += (a ** digit_count)
    return sum 
num = int(input("Enter The Number: "))      
ans = Armstrong(num)
if ( ans == num):
    print(f"YES!!, The Given Number {num} is Armstrong Number : {ans}")
else:
    print(f"NO!!!, The Given Number {num} is Not Armstrong Number : {ans}")