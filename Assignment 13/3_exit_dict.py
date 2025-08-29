# Python Program to Check if a Given Key Exists in a Dictionary or Not.

dict1 = {"a" : 1, "b" : 2, "c" : 5, "d" : 8}

check_key = input("ENTER THE KEY: ")

if check_key in dict1:
    print(f"GIVEN KEY EXIST IN A DICTIONARY {check_key}")
else:
    print(f"GIVEN KEY DOES NOT EXIST IN A DICTIONARY {check_key}")
    