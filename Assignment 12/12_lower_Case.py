# Python Program to count number of lowercase characters in a string.

str1 = input("ENTER THE STRING: ")
c_lower = 0

for i in str1:
    if i.islower():
        c_lower+= 1
        
print(c_lower)