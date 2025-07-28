# Write a program to check if entered year is a leap year or not.

def leapYear(num):
    if num % 4 == 0:
        print("Yes, it is leap year")
    else:
        print("NO, it is Not leap Year: ")

num = int(input("Enter The Any Year: "))
leapYear(num)