P = float(input("Enter the principle amount:"))
Time = float(input("Enter the Time in year:"))
Rate = float(input("Enter the rate of interest:"))

A = P * (1 + Rate / 100) ** Time
compound_interest = A - P 

print("compound interest is:", compound_interest)