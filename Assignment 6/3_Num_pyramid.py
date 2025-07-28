
    
for i in range(4):
    for j in range(4 - i - 1):
        print("  ", end="")

    num = 1  
    for k in range(i + 1):
        print(num, end="   ")
        num = num * (i - k) // (k + 1)
    print()