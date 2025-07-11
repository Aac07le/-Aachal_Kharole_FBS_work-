# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

subject1 = int(input("Enter marks for subject1: "))
subject2 = int(input("Enter marks for subject2: "))
subject3 = int(input("Enter marks for subject3: "))
subject4 = int(input("Enter marks for subject4: "))
subject5 = int(input("Enter marks for subject5: "))

total_mark = (subject1 + subject2 + subject3 + subject4 + subject5)
max_mark = 5 * 100

percentage = (total_mark / max_mark) * 100
print("percentage: ", percentage)

per = int(input("Enter percentage number: "))

if(per >= 80 and percentage <= 100):
    print("with Distinction")
    
elif(per >= 60 and percentage <= 70):
    print("with Higher class: ")
        
elif(per >= 50 and percentage <= 60):
    print("with first class: ")
    
elif(per >= 40 and percentage <= 60):
    print("with second class")
    
elif(per <=30 and percentage >=0):
    print("Fail: ")
else:
   print("Wrong input")
    

