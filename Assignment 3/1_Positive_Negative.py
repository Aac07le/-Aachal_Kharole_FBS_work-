# Write a program to check if the given number is positive or negative.

num = int(input("Enter Any Number: "))

if(num > 0):
    print("Given Number is Positive: ")
    
elif(num < 0):
    print("Given Number is Negative: ")
    
elif(num == 0):
    print("Given Number is Neutral:")
    
else:
    print("Wrong Input")