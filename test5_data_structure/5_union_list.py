# Python Program to Find the Union of two Lists without using set concept.


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
for i in list2:
    if i not in list1:
        list1.append(i)
        
print(list1)