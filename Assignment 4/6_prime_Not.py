
# WAP to check if a given number is prime number or not.

num = int(input("Enter Any Number: "))

for i in range(2,num):
  if num % 2 == 0:
    print("Not Prime Number: ")
    break
else:
 print("Prime Number: ")