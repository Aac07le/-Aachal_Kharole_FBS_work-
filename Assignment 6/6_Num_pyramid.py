
count = int(input("Enter the count of pyramid numbers: "))

for i in range (1, count+1):
    if i % 2 == 0:
        continue
    
    for j in range(1, count + 2 -i):
        print(" ",end=" ")
        
    for j in range(1, i+1):
        print("", j ,"", end=" ")
    print()