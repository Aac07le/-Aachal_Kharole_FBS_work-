
 
# Write a program to remove all occurrences of a given element in the list.

list1 = [10,20,40,50,10,33,10]

element = int(input("Enter the number: "))

c = list1.count(element)

for i in range(c):
    list1.remove(element)
    
print(f"AFTER REMOVE ALL THE OCCURANCES OF THE  ELEMENT THE LIST1 IS {list1}")