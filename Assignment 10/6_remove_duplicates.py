# Write a program to remove duplicates from the list.

list1 = [20,30,40,30,50,60,50,40,50,60,70,80,90]
element = int(input("ENTER THE ANY NUMBER: "))
c = list1.count(element)
for i in range(c):
    list1.remove(element)
print("list1 = [20,30,40,30,50,60,50,40,50,60,70,80,90]")
print(f"AFTER REMOVE THE LIST IS {list1}")


# while element in list1:
#     list1.remove(element)
# print(f"AFTER REMOVE THE LIST IS {list1}")