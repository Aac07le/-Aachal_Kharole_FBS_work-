# Python Program to Replace all Occurrences of ‘a’ with $ in a String.

str1 = input("ENTER THE STRING: ")

for a in str1:
    new_str2 = str1.replace('a','&')
    
print(f"AFTER REPLACEING a WITH $ THE NEW STRING IS: {new_str2}")