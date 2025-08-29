# Given two sets of numbers, write a Python program to find the missing numbers in the 
# second set as compared to the first and vice versa. Use the Python set.

set1 = {3,5,2,7,9,6,10,15,12}
set2 = {5,45,6,89,10,2,9,14}

print("MISSING IN SET2 AS COMPAIRE SET1")
for i in set2:
     if i not in set1:
        print(i)
        
print("MISSING IN SET1 AS COMPAIRE SET2")        
for j in set1:
    if j not in set2:
      print(j)    
