# Write a program to print all numbers which are divisible by m and n in the list.

list1 = [2,4,6,3,56,20,12,25,68,60,50]
list2 = []
list3 = []
m = int(input("enter the any number: "))
n = int(input("Enter the any number: "))

for i in range(len(list1)):
    if list1[i] % m == 0 and list1[i] % n == 0:
        list2.append(list1[i])
        
    # if list1[i] % n == 0:
    #     list3.append(list1[i])
        
print("AFTER ALL ELEMENTS IN THE LIST DIVIDING BY m AND n THE LIST IS:= ", list2)
# print(list3)