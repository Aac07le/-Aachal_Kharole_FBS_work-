# Count the number of spaces in a string (take input from user).

str1 = input("ENTER THE STRING: ")
count = 0
# for i in str1:
#   if i.isspace():
   
#     count = count + 1
    
# print(count) 

count = sum (1 for i in str1 if( i.isspace()))
print(count)
