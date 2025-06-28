
# Convert distant given in feet and inches into meter and centimeter.
feet = int(input("Enter the valu for feet: "))
inches = int(input("Enter the valu for inches: "))

total_inches = feet * 12 + inches
total_centimeter = total_inches * 2.54
meter = total_centimeter / 100

print("meter:", meter)
print("total_centimeter: ", total_centimeter)