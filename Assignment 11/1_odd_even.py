# Python Program to Put Even and Odd elements of a List into two Different Lists.
def evenOdd():
    list1 = []
    list2 = []
    list3 = []
    num = int(input("\n ENTER A NUMBER FOR HOW MANY ELEMENTS YOU HAVE IN LIST: "))
    for i in range(num):
        ele = int(input("Enter The Number: "))
        list1.append(ele)
    print(f"\n THE ORIGINAL LIST IS:= {list1} \n ") 

    for i in range(len(list1)):
        
        if (list1[i] % 2==0):
         list2.append(list1[i]) 
         
        if (list1[i] % 2 != 0):
         list3.append(list1[i])
            

    print(f" AFTER PUTTING EVEN NUMBER IN THE LIST IS:= {list2} \n")
    print(f" AFTER PUTTING ODD NUMBER IN THE LIST IS:= {list3} \n ")
    
evenOdd()