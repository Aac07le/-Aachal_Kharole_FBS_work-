# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
# (input("Enter the ticket price: "))
age1 = int(input("Enter The age1 of Passenger: "))
age2 = int(input("Enter The age2 of Passenger: "))
age3 = int(input("Enter The age3 of Passenger: "))
age4 = int(input("Enter The age4 of Passenger: "))
age5 = int(input("Enter The age5 of Passenger: "))

amount = (age1 + age2 + age3 + age4 + age5)
fair = 0

print("amount: ", amount)

if(age1 < 12):
    fair += amount - amount * 0.3

elif(age1 > 59):
    fair += amount - amount * 0.5
    
else:
    fair += amount
    
if(age2 < 12):
    fair += amount - amount * 0.3
    
elif(age2 > 59):
    fair += amount - amount * 0.5
    
else:
    fair += amount
    
if(age3 < 12):
    fair += amount - amount * 0.3

elif(age3 > 59):
    fair += amount - amount * 0.5
    
else:
    fair += amount

if(age4 < 12):
    fair += amount - amount * 0.3

elif(age4 > 59):
    fair += amount - amount * 0.5
else:
    fair += amount

if(age5 < 12):
    fair += amount - amount * 0.3

elif(age5 > 59):
    fair += amount - amount * 0.5
else:
    fair += amount
    print("Fair", fair)
    