# Program to find all perfect numbers till the given number

num_count = int(input("Enter maximum number till which we need to find perfect numbers: "))


for num in range(1, num_count+1):
    sum_of_divisior = 0
    for i in range(1, num):
        if num % i == 0:  
            sum_of_divisior += i
        

    if sum_of_divisior == num:
        print(f"{num} is a PERFECT NUMBER!!!")
    # else:
        # print(f"No, {num} is NOT a PERFECT NUMBER!!!")
    




    