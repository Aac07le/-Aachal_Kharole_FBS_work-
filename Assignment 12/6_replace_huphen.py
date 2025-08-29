# Python Program to Take in a String and Replace Every Blank Space with Hyphen.


str1 = input("ENTER THE STRING:= ")

for i in str1:
    str2 = str1.replace(' ', '-')
    
print(str2)