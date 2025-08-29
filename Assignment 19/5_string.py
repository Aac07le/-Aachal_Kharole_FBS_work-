# Find all of the words in a string that are less than 5 letters (take input from user).

str1 = input("ENTER THE STRING:")
words = str1.split()

word_string = [word for word in words if len(word) < 5]

print("THE WORD IN A LIST THAT ARE LESS THAN FIVE LETTERS: ",word_string)