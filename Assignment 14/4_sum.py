# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

list1 = [2,4,6,8,5,10]

value = int(input("ENTER THE ANY VALU WHICH YOU WANT: "))

pairs_of_elements = []

for i in range (len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == value:
            pairs_of_elements.append((list1[i], list1[j]))
    
    
if pairs_of_elements:
     print(f"THE SUM OF PAIRS {[value]} : {[pairs_of_elements]}")
     
   
else:
    print(f"NO PAIRS FOUND WITH SUM EQUAL TO {value}")