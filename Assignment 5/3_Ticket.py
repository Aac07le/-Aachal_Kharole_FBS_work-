# Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

No_of_Passenger = int(input("Enter Number of passenger:"))
Ticket_cost = int(input("Enter per ticket cost:"))

total_amount = 0

for i in range (1,No_of_Passenger+1):
    print(f"For Passenger {i}")
    age_total = 0
    age = int(input("Enter The age1 of Passenger: "))
    

    amount = age_total
    
  
    if age < 12:
        amount = Ticket_cost * 0.3   
    elif age > 59:
        amount = Ticket_cost * 0.5  
    else:
        amount = Ticket_cost        

    total_amount += amount

print("\nTotal amount for all passengers:", total_amount)   