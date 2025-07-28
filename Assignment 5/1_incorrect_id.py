# Write a program to prompt user to enter userid and password. 
# If Id and password is incorrect give him chance to re-enter the credentials. 
# Let him try 3 times. After that program to terminate.
    
    
for i in range(1, 5):
    if i == 4:
        print("You have entered wrong credentials 3 times, so Exiting!")
        break
        
    userid = str(input("Enter The User Id: "))
    password = str(input("Enter The Password: "))

    if userid == "fbs" and password == "fbs123":
        print("Credentials are correct.")
        print("You have successfully logged in. Thanks!")
        break
    else:
        print("Login credentials are incorrect, please enter again!")
        continue
    
    
    
    