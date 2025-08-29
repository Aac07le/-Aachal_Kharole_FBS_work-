# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("ENTER THE NUMBER: "))
dict1 = {}

for x in range(1,n +1):
    dict1[x] = x * x

print(f"GENERATING THE DICTIONARY: {dict1}")
