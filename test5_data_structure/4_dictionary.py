# There is a list with some numbers. Create a new dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that number in list.
# [1,3,4,1,2,3,6,7,1,2,4]
# {1:3,3:2,2:2,

list1 = [1,3,4,1,2,3,6,7,1,2,4]
dict1  = {}

for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
        
print(dict1)