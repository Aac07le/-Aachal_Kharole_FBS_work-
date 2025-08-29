# Python Program to Sort the List According to the Second Element in Sublist.

def bubbleSort():
    list1 = [[1,4], [2,3], [4,5] , [6,7] , [6,10]]
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j][1] > list1[j+1][1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                
    return (f"After Sort the List According to the Second Element in Sublist { list1}")
                
result = bubbleSort()
print(result)
            
    