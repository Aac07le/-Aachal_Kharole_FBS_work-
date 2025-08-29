# Python Program to find larger string without using built-in functions.

str1 = input("ENTER THE STRING: ")

str2 = input("ENTER THE STRING:")

c_str1 = 0

c_str2 = 0

for i in str1:
  c_str1 += 1
for j in str2:
  c_str2 += 1
    
if c_str1 > c_str2:
    print("STRING1 IS LARGER")
else:
    print("STRING2 IS LARGER")