# count = int(input("Enter the count of pyramid numbers: "))

# for i in range (1,count+1):
#     if i % 2 == 0:
#         continue
    
#     for j in range(1,count -i):
#         print(" ",end=" ")
        
#     for j in range(1,i-1):
#         print("", i,"",end=" ")
#     print()
    
    
for i in range(1, 5 + 1):
    for j in range(5 - i):
        print("  ", end="")
    k= i
    for j in range(1, i + 1):
        print(k, end=" ")
        k += 1

    k-= 2  # step back one extra to start decreasing
    for j in range(1, i):
        print(k, end=" ")
        k -= 1

    print()