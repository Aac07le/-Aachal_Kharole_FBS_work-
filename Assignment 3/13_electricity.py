
# Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

unit = int(input("Enter unit of Electricity: "))

if(unit <= 50):
    bill = unit * 0.5
elif(unit > 50 and unit <= 150):
    bill = 50 * 0.5
    unit = unit - 50
    bill += unit * 0.75
elif(unit > 150 and unit <= 250):
    bill = 50 * 0.5
    unit = unit - 50
    bill += 100 * 0.75
    unit = unit - 100
    bill += unit * 1.20
elif():
    bill = 50 * 0.5
    unit = unit * 50
    bill = 100 * 0.75
    unit = unit - 100
    bill = 100 * 120
    unit = unit - 100
    bill += unit * 1.50
bill = bill + (bill * 0.20)
print(bill)
    

    
    