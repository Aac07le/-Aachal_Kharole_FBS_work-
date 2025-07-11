# WAP to check if given number Strong Number.

num = int(input("Enter any Number: "))
sum = 0
temp = num

while(num != 0):
    a = num % 10
    num = num // 10
    fact = 1
    
    for i in range(1,a + 1):
     fact = fact * i
     
    sum = sum + fact

if (sum == temp):
    print(f"Yes,{sum} is a STRONG NUMBER !!!: ")
    
else:
    print(f"No, {sum} is NOT STRONG NUMBER!!: ")

       