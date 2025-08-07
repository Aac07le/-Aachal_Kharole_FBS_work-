# WRITE A PROGRAM TO WHICH WE PASS A PARAMETER AND PRINT THE FACTOR OF GIVEN NUMBER.

def factor(num):
    
    for i in range(1,num+1):
       if num % i == 0:
           
        print(i)
    
num = int(input("ENTER THE NUMBER: "))
factor(num)