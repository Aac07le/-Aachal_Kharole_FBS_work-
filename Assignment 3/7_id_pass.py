
# Write a program to check if user has entered correct userid and password.

correct_userid = "Achal@123"
correct_password = "1997"


userid = str(input("Enter The Your  Userid: "))
password  = str(input("Enter The Your Password: "))

if (userid == correct_userid and password == correct_password ):
    print("Your Userid is Correct: ", userid)
    # print("your password is coorect: ", password)
    
else:
    print("Invalid Userid or Password: ")


    