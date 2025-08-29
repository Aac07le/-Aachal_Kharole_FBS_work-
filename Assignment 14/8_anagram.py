# Write a Python program to find all the anagrams and group the together from a given list of strings.

 
list1 = ["listen", "silent", "car", "arc", "Aachal"]


anagram_groups = {}

for word in list1:
    key = "".join(sorted(word.lower()))  
    if key not in anagram_groups:
        anagram_groups[key] = []
    anagram_groups[key].append(word)


for group in anagram_groups.values():
    print(group)