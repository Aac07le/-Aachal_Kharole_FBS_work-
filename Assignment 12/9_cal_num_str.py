# Python Program to Calculate the Number of Words and the Number of Characters Present in a String.

str1 = input("ENTER THE STRING: ")

c_words = len(str1.replace(" ", " "))
c_charecter = len(str1.split())


print(c_charecter)
print(c_words)