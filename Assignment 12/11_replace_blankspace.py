# Python Program to replace every blank space with hyphen in a string.

str1 = input("ENTER THE STRING: ")

for i in str1:
    new_str1= str1.replace(' ','-')
        
print(new_str1)