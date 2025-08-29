# Python Program to Remove the Given Key from a Dictionary.

dict1 = {1 : "Apple", 2 : "mango", 3 : "orange", 4 : "banana", 5 : "grapes"}

key = int(input("ENTER THE KEY:=  "))

if key in dict1:
    dict1.pop(key)
    print(key," key remove in dictionary")
else:
    print(key," NOT FOUND IN DICTIONARY")
     
 
    
print(" AFTER REMOVE GIVEN KEY THE UPDATED DICTIONARY IS:= " ,dict1)