# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindrome_generator():
    num = int(input("ENTER THE NUMBER:"))
    while True: 
        if str(num) == str(num)[::-1]: 
            yield num
        num += 1

gen = palindrome_generator()

for _ in range(20):
    print(next(gen), end=" ")
    print(next(gen), end=" ")
    