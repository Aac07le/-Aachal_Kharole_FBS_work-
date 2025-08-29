# Write a program to find maximum and minimum element in a list.

list1 = [10,5,68,90,45,30,20,56,96,2]

min_element = 10
max_element = 10

for i in range(1,len(list1)):
    
     if (list1[i]) < min_element:
        min_element = list1[i]
    
     if list1[i] > max_element:
           max_element = list1[i]
             
        
print(f"THE MINIMUM NUMBER IN LIST1 IS:  {min_element}")
print(f"THE MAXIMUM NUMBER IN LIST1 IS:  {max_element}")

