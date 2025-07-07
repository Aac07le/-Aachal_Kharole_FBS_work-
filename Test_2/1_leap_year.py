# leap year or not

year = int(input("Enter a year: "))

if(year % 400 == 0):
   print("It is Leap year: ")
elif(year % 100 == 0):
    print("It is Not Leap Year: ")
elif(year % 4 == 0 ):
    print("It is Leap Year: ")
else:
    print("It is Not Leap Year: ")