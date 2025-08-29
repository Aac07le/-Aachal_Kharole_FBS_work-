# Python Program to Count the Number of Vowels in a String.

str1 = input("ENETR THE STRING:= ")

c_num_vowel = 0

for  i in str1:
    if i in "aeiou":
        c_num_vowel += 1
        
print(c_num_vowel)