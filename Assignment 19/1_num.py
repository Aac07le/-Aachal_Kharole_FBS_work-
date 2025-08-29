# Find all of the numbers from 1–1000 that are divisible by 8.

list1 = []
num = int(input("enter the number: "))
for x in range(1,num):
    list1.append(x)
# print(list1)

list1 = [x for x in list1 if (x % 8 == 0)]
print(list1)