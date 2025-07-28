
# Write a program to print prime numbers between 1 to 100.

num = 2

while num <= 100:
  prime = True
  i = 2
  while i <= (num ** 0.5):
    if num % i == 0:
      prime = False
      break
    i += 1
  if prime:
    print(num)
  num += 1
  
  
# for num in range(2, 100+1):
#     prime = True
#     for i in range(2,int(num ** 0.5)):
#       if num % i == 0:
#         prime = False
#         break
#       if prime:
#         print(num)