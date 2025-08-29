# Write a program to print list after removing even numbers.


def even(num):
    list1 = []
    for i in range(1,num):
        list1.append(i)
    print("\n LIST1 IS " ,list1)

    for i in list1:
        if i % 2 == 0:
            list1.remove(i)    
    print(f"\n AFTER REMOVING EVEN NUMBER IN THE LIST {list1} \n")
    

num = int(input("\n ENTER HOW MANY ELEMENTS YOU HAVE IN THE LIST: "))
even(num)