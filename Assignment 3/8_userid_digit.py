#  Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed.

import random

userid = (input("Enter the your  UserId: "))
password  = (input("Enter the your password: "))

if (userid == "aachal@123" and password == "1997"):
   
   print("Login Successfully")
    
   Captcha = random.randint(1000, 9999)
   
   print("enter this number: ", Captcha)
   user_input  = int(input("Enter Captcha:"))
    
   if user_input == Captcha:
    print("Successful ! Welcome")
    
   else:
    print("Verification Failed ! Number Do Not Match: ")
         
else:
 print("Invalid UserId or Password: ")
