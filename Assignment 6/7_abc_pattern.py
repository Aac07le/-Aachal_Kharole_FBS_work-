
for i in range (1, 10+1):
    if i % 2 == 0:
        continue
    
    for j in range(1,10 + 2 -i):
        print(" ",end=" ")
    x = 65    
    for j in range(1, i+1):
        print("",chr(x),"",end=" ")
        x += 1
    print()