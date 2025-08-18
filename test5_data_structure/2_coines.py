# A teacher came to class with a large box tokhat has several coins. Each coin has a number printed on it.
# Before coming to class, she ensured that All the numbers occur an Even number of times. However, 
# while coming to the class, one coin fell down and got lost. She wants to find out the number on the missing coin.
# Inputs:
# The original number of coins and the actual
# number on each of the coins, separated by spaces.
# Output: The number on the missing coin
# Sample Input: 8
# 5 7 2 7 5 2 5
# Sample Output: 5

num = int(input("ENTER THE NUMBER OF COINS WHICH IS EVEN: "))
list1 = []
if num % 2== 0:
 print("ENTER THE NUMBER ON THE COINS: ")
 for i in range(num - 1):
        n = int(input("Enter the number of coins: "))
        list1.append(n)
    
 set1 = set(list1)
    
 for x in set1:
    if list1.count(x) % 2 != 0:
     print("THE MISSING COIN IS: ",x)
                
else:
    print("ENTER EVEN NUMBER OF COINS: ")
    
            