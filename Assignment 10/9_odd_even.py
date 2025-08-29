# Write a program of having n number of elements in the list and find out even and odd elements
# in that list and then create two separate lists which will have even elements and other will have odd elements.

list1 = [2,34,37,8,9,55,44,30,6,23,12,15]
list2 = []
list3 = []
for i in range(len(list1 )-1):
    if list1[i] % 2 == 0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
        
print(f"THE ORIGINAL LIST IS {list1}")        
print(f"THE EVEN ELEMENTS IN THE LIST1 IS {list2}")
print(f"THE ODD ELEMENTS IN THE LIST1 IS {list3}")