# Write a program to calculate profit or loss.

SP = int(input("Enter Selling Price of Product: "))
CP = int(input("Enter Cost Price of Product: "))

if SP > CP:
    profit = SP - CP
    print("Profit")
    
elif CP > SP:
    loss = CP - SP
    print("Loss")
    
else:
    print("Not Profit Not Loss")