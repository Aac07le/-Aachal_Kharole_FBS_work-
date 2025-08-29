# Write a program to print list after removing even numbers.

list1 = [2,4,3,6,7,8,5,10,12,55,46,37]
list2 = []
for i in range(len(list1)-1):
    if (list1[i] % 2 != 0):
        list2.append(list1[i])
        
print(list2)
    
    