# Python Program to Sum All the Items in a Dictionary.

dict1 = {"items1" : 1, "items2" : 4, "items3" : 7, "items4" : 8, "items5" : 45}


sum_of_all_items = 0
for values in dict1.values():
    sum_of_all_items += values
    
print(dict1.keys())

print(dict1.values())

print(f"THE SUM OF ALL ITEMS is {sum_of_all_items}")
