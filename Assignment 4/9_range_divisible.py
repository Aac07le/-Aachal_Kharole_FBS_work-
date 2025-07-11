# WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter any number: "))

stop = int(input("Enter Any Number: "))

n = int(input("Enter any Number: "))

print("All Numbers in a range divisible by Number: ")

for i in range(start,stop+1):
    if i % n == 0:
        print(i)