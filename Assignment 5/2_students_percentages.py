
num_of_std = int(input("Enter the number of students: "))

total_percentage = 0


for i in range(1, num_of_std + 1):
    print(f"\n\nFor Student {i}:\n")
    
    sub1 = int(input("Enter marks for Subject 1, out of 100: "))
    sub2 = int(input("Enter marks for Subject 2, out of 100: "))
    sub3 = int(input("Enter marks for Subject 3, out of 100: "))
    sub4 = int(input("Enter marks for Subject 4, out of 100: "))
    sub5 = int(input("Enter marks for Subject 5, out of 100: "))
    percentage = ((sub1 + sub2 + sub3 + sub4 + sub5) / 500) * 100
    
    # sub_total = 0
    # for j in range (1, 6):
    #     sub = int(input(f"Enter marks for Subject {j}, out of 100: "))
    #     sub_total += sub
    # percentage = ((sub_total) / 500) * 100
    
    print(f"\nPercentage of Student {i} = {round(percentage, 2)}%")
    total_percentage += percentage
    
avg_percentage = (total_percentage / (num_of_std * 100)) * 100

print(f"\n\nAverage percentage of all students = {round(avg_percentage, 2)}%\n\n")
    
