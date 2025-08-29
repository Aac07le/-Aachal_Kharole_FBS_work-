# Accept a number from user and check if this element is present in the list or not. 
# Also tell how many times it is present in the list.

list1 = [20,30,40,60,40,40,45,68,90]
element = int(input("ENTER THE ANY NUMBER: "))

# METHOD 1--------------------------------------------------------:
c =0    
present = False

for i in list1:
    if element == i:
        present = True
        c += 1
   
if present:
    print(f"YES, THE GIVEN ELEMENT {element} IS PRESENT IN THE LIST, {c} TIMES")
else:
    print(f"NO, THE GIVEN ELEMENT {element} NOT PRESENT IN THE LIST")
    
# METHOD 2----------------------------------------------------------:
new_list = [x for x in list1 if x == element]
print(f"Present, {len(new_list)}  times") if new_list else print(f"Not present!")


    
    