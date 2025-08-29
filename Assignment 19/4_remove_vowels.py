# Remove all of the vowels in a string (take input from user).


str1 = input("ENTER THE STRING: ")
vowels = "aeiouAEIOU"
result = " ".join([i for i in str1 if i not in vowels])
print(result)
