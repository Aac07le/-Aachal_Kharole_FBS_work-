# Write a program to create a duplicate of an existing list. It should not point to same list.

original_list1 = [10,20,30,40,50,60]
duplicate_list2 = []


for i in range(len(original_list1)):
    
  duplicate_list2.append(original_list1[i])

print(f"THE ORIGINAL LIST1 IS {original_list1}\n")

print(f"THE DUPLICATE LIST1 IS {duplicate_list2}")

