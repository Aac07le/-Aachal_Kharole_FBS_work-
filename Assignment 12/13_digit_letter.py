# Python Program to count number of digits and letters in a string.

str1 = input("ENTER THE STRING: ")

c_digit = 0

c_letter = 0


for i in str1:
    if i.isdigit():
        c_digit+= 1
        
    elif i.isalpha():
        c_letter +=1
        
print(f"NUMBER OF DIGIT IN GIVEN STRING IS := {c_digit} ")

print(f" NUMBER OF LETTERS IN GIVEN STRING IS := {c_letter} ")