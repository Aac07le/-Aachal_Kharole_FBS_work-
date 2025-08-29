# Write a Python program to remove the intersection of a second set with a first set.

set1 = {1,2,3,4,5,"Aachal", "mahima"}

set2 = {1,5,6,7,8,"Aaku", "puja"}

# set1 = set1 - set2

set1.difference_update(set2)
print(set1)


# set1 = {1,2,3,4,5,"Aachal", "mahima"}
# set2 = {1,5,6,7,8,"Aaku", "puja"}

# for i in set2:
#     if i in set1:
#         set1.remove(i)
        
# print(set1)
        