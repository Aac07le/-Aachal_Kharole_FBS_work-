# WAP to accept Three digit number. 
# if first digit is double of second digit and half of third digit then display "Yes, you have done it"
# otherwise display "Please try next time."

num = int(input("Enter Three digit Number: "))

a = num // 100 
b = (num // 10) % 10
c = num % 10

print("Enter the valu of a:", a)
print("Enter the valu of b: ", b)
print("Enter the valu of c: ", c)


if a  ==  2 * b and a == c / 2:
    print("Yes, You have done it: ")
else:
    print("Please Try Next Time: ")
