# Write a program to create three lists of numbers, their squares and cubes.
list1 = [2,3,4,5,6,7,8]
list2 = []
list3 = []

for i in range(len(list1)):
        squere = list1[i] **2
        list2.append(squere)
        cube = list1[i] ** 3
        list3.append(cube)
        
print(list1)            
print("THE SQUERE OF ELEMENTS IN  LIST1: ",list2)          
print("THE CUBE OF ELEMENT IN LIST1 : ",list3)        