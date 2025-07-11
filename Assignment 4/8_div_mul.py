# write a Program to find which number is divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter any Number for start: "))
stop = int(input("Enter any number for stop: "))

# n = int(input("Enter any range: "))
print("The Number is Divisible by 7 and multiple of 5: ")

# for i in range(1,n + 1):
for i in range(start,stop+1):  
    
    if (i % 7 == 0 and i % 5 == 0):
     print(i)
        
        