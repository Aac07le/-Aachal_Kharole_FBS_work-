# Find all of the numbers from 1–1000 that have a 6 in them.

list1 = []
num = int(input("Enter the number: "))
for x in range(1,num):
    list1.append(x)
list1 = [x for x in list1 ]
print(list1)