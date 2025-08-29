# Python Program to Find the Second Largest Number in a List Using Bubble Sort.

def bubleSort():
    list1 = []
    num = int(input("ENTER HOW MANY ELEMENTS YOU HAVE IN LIST: "))
    for i in range(num):
        ele = int(input(f"Enter element {i + 1}: "))
        list1.append(ele)
     
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j] > list1[j+1]:
               list1[j], list1[j + 1] = list1[j + 1], list1[j]
                
    print("sorted list:",list1)
    print("Second largest Number is: ", list1[-2])
    
bubleSort()

