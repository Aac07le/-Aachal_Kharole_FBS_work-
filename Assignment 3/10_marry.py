
# WAP to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

age_male = int(input("Enter age for the male: "))
age_female = int(input("Enter age for the female: "))

if(age_male >= 21 and age_female >= 18 ):
    print("Both are eligible for marry: ")
else:
    print("Not eligible: ")