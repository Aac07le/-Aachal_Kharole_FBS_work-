# Write a program to create three lists of numbers, their squares and cubes.

def squereCube(num):
   list1 = []
   list2 = []
   list3 = []
 
   for  i in range(1,num+1):
        list1.append(i)
        
   print(f"\n LIST1 IS:= {list1} \n")
   
   for i in range(len(list1)):
      square =  list1[i] ** 2
      
      list2.append(square)
      
      cube = list1[i] ** 3
      
      list3.append(cube)
      
   print(f" THE ORIGINAL ELEMENTS IN THE LIST IS:=  {list1} \n")  
     
   print(f" SQUARE OF ALL ELEMENTS IN THE LIST IS:=  {list2} \n")
   
   print(f" CUBE OF ALL ELEMENTS IN THE LIST IS:=  {list3} \n")
   
num = int(input("\n ENTER HOW MANY NUMBER YOU HAVE IN THE LIST : "))

squereCube(num)
   
   