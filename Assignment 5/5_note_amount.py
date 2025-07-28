# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amount = int(input("Enter The amount number:"))

# # EXISTING CODE:
# n500, n200, n100, n50, n20, n10 = 0,0,0,0,0,0

# # 500
# n500 = amount // 500
# amount = amount % 500

# # 200
# n200 = amount // 200
# amount = amount % 200

# # 100
# n100 = amount // 100
# amount = amount % 100

# # 50
# n50 = amount // 50
# amount = amount % 50

# # 20
# n20 = amount // 20
# amount = amount % 20

# # 10
# n10 = amount // 10
# amount = amount % 10

# print(f"Number of notes:\n500 x {n500}\n200 x {n200}\n100 x {n100}\n50 x {n50}\n20 x {n20}\n10 x {n10}")

# # ----- NEW CODE USING LOOP
# notes = [500, 200, 100, 50, 20, 10]

print("Number of notes:")
for i in (500, 200, 100, 50, 20, 10):
    count = amount // i
    amount = amount % i
    print(f"{i} x {count}")
    
if amount > 0: 
    print(f"Remaining coins x {amount}")
    
print("Thanks!!!")
    


    