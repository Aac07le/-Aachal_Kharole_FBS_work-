# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.

str1 = input("\n ENTER THE STRING: ")

str2 = input("\n ENTER THE STRING: ")

c_cal_str1 = 0

c_cal_str2 = 0


for i in str1:
    c_cal_str1 += 1
for j in str2:
    c_cal_str2 += 1
    
if c_cal_str1 > c_cal_str2:
    print(f"\n STRING1 {str1} IS THE LARGEST STRING ")
else:
    print(f"\n STRING2 {str2} IS THE  LARGEST STRING")
        
