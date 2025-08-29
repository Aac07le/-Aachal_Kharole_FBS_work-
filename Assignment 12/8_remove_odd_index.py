# Python Program to Remove the Characters of Odd Index Values in a String.

str1 = input("ENTER THE STRING: ")
str2 = ""
for i in range(len(str1)):
    if i % 2 == 0:
        str2 += str1[i]
        
print(str2)
