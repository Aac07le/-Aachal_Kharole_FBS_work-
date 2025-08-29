# Python Program to Multiply All the Items in a Dictionary.

dict1 = {"a" : 4, "b" : 4, "c" : 2}
result = 1

for values in dict1.values():
    result *= values

print(dict1)
print(f" AFTER MULTIPLY ALL THE VALUES THE DICTIONARY IS {result}")

