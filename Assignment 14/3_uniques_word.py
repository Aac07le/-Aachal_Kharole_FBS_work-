# Write a Python program to find all the unique words
# and count the frequency of occurrence from a given list of strings. 
# Use Python set data type.

list1 =["firstbit" , "solution" , "python" , "solution", "python"]
unique_words = set(list1)

print("Unique Words and their Frequencies:")
for word in unique_words:
    print(f"{word} : {list1.count(word)}")