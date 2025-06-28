# WAP to calculate selling price of book based on cost price and discount.
discount = int(input("Enter the discount: "))
C = int(input("Enter the cost price of book: "))

# calculate discount amount
discount_amount = (discount / 100) * C

# calculate selling price
selling_price = C - discount_amount 

print("The selling price is: ", selling_price)
