# Python Program to Find the Union of two Lists
list1 = [5,6,3,4,8,12,50,65,55]

list2 = [3,67,65,50,6,4,8,90,80]
list3 = []
ele = 0
for  i in list1:
    if i not in list2:
     list3.append(i)
print("Union of Two list", list3)