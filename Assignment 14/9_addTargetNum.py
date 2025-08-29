# Write a Python program to find all the unique combinations of 3 numbers 
# from a given list of numbers, adding up to a target number.

list1 = [2,4,6,8,5,10,12,3,9]

value = int(input("ENTER THE ANY VALU WHICH YOU WANT: "))

triplet_of_elements = []

for i in range (len(list1)):
    for j in range(i + 1, len(list1)):
        for x in range(j + 1, len(list1)):
         if list1[i] + list1[j] + list1[x] == value:
            triplet = tuple(sorted((list1[i], list1[j],list1[x])))
            if triplet not in triplet_of_elements:
                triplet_of_elements.append(triplet)
    
    
if triplet_of_elements:
     print(f"THE SUM OF PAIRS {[value]} : {[triplet_of_elements]}")
     
   
else:
    print(f"NO PAIRS FOUND WITH SUM EQUAL TO {value}")