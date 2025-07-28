
for i in range(1, 5 + 1):
    # Leading spaces
    for j in range(5- i):
        print("  ", end="")

    if i == 5:
        # Last row: print all numbers with equal spacing
        for j in range(1, 5 + 1):
            print(j, end="   ")
    else:
            print("1", end="")
    for j in range((i - 1) * 4 - 1):
            print(" ", end="")

    if i != 1:
        print(i, end="")
    
    print()