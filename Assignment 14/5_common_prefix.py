# Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_common_prefix(strings):
    if not strings:
        return ""
    
   
    shortest = min(strings, key=len)
    
    prefix = ""
    for i in range(len(shortest)):
        
        words = {s[i] for s in strings}
        
        if len(words) == 1:  
            prefix += words.pop()
        else:
            break
    return prefix

words = input("Enter strings separated by spaces: ").split()
result = longest_common_prefix(words)
print("Longest Common Prefix:", result if result else "No common prefix")
