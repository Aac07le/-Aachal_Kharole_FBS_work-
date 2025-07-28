
for i in range(1,6+1):
    for j in range(1,6):
        if j == 1  or j == 6 - 1 or i == 1 or i == 7 -1:
            print(" * ", end=" ")
        else:
            print("   ", end=" ")
    print()


# *   *   *   *   *  
# *               *
# *               *
# *               *  
# *               *
# *   *   *   *   *