# Python Program to Merge Two Lists and Sort it.

    
list1 = [3,5,1,8,10,15,28,69]
list2 = [4,6,7,9,55,30,90,100]
list3 = []

for i in range(len(list1)):
    for j in range(len(list1)):
       list3=  list1 + list2
       list3.sort()
       
print(f"\n BEFORE MERGE AND SORT THE LIST IS: {list1}")

print(f"\n BEFORE MERGE AND SORT THE LIST IS: {list2}")

print(f"\n AFTER MERGE TWO LIST AND SORT IT THE LIST IS {list3} \n")
    
    
    