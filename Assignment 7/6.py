
for i in range(1, 5 + 1):
    if i == 1:
        for j in range(1, 5 + 1):
            print(j, end=" ")
    else:
        print(i, end=" ")
        for j in range(1, 5 - i):
            print(" ", end=" ")
        if i != 5:
            print(5, end="")
    print()