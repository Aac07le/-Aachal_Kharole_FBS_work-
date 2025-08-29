# Write a Python program to find elements in a given set that are not in another set.

set1 = {2,4,5,9,12,34}
set2 = {10,5,13,12,2}
for i in set1:
    if i not in set2:
        
      print(i,"IS NOT IN SET2: ")
