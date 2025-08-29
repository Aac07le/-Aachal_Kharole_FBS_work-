# Python Program to Form a New String where the First Character and the Last Character have been Exchanged.

str1 = input("Enter the string: ")
if len(str1) < 2:
    str2 = str1
else:
    str2 = str1[-1] + str1[1:-1] + str1[0]
    
print(str2)
        