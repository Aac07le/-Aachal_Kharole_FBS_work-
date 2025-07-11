
# WAP to print factorial of a number .

num = int(input("Enter the valu for num: "))
print("Factorial number is to: ")

fact = 1

for i in range(1,num+1):
    
    fact = fact * i
    
    print(fact)
    
print("end")
    