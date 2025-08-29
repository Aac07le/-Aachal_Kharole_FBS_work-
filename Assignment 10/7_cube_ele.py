# Write a program to create a new list from existing list which contains cube of each number of list.

list1 = [2,3,4,5,6,7,8]
list2 = []
for i in range(len(list1)):
    cube = list1[i] ** 3
    list2.append(cube)
         
        
print(list2)