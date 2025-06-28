
# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

amount = int(input("Enetr the amount: "))

# 500
n500 = amount // 500
amount = amount % 500

# 200
n200 = amount // 200
amount = amount % 200

# 100
n100 = amount // 100
amount = amount % 100

# 50
n50 = amount // 50
amount = amount % 50

# 20
n20 = amount // 20
amount = amount % 20

# 10
n10 = amount // 10 
amount = amount % 10

print("Enter the no. of 500 Notes: ", n500)
print("Enter the no. of 200 Notes: ", n200)
print("Enter the no. of 100 Notes: ", n100)
print("Enter the no. of 50 Notes: ", n50)
print("Enter the no. of 20 Notes: ", n20)
print("Enter the no. of 10 Notes: ", n10)
