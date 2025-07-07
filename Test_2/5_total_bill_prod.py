
# A man goes for shopping. 
# He buys 5 products.
# Accept the price of all products and display the total bill after adding 18% GST.

product1 = int(input("Enter the price of first product1: "))

product2 = int(input("Enter the price of first product2: "))

product3 = int(input("Enter the price of first product3: "))

product4 = int(input("Enter the price of first product4: "))

product5 = int(input("Enter the price of first product5: "))

GST = 0.18

total_price = product1 + product2 + product3 + product4 + product5

total_bill = total_price *(1 + GST)

print("total bill of all five product is: ", total_price)

print("total bill of all product with GST is: ", total_bill)