# Write a program to find the second largest element in the list.

list1 = [12,34,55,68,90,98,100,56]

max = list1[0]
sec_max = 0 
for i in range(1,len(list1)):
    if (max < list1[i]):
        sec_max = max
        max = list1[i]
    elif (sec_max < list1[i]):
        sec_max = list1[i]
        
print(sec_max)