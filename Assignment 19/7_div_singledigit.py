# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

# Nested list comprehension
divisible_numbers = [x for x in range(1, 1001) if any(x % y == 0 for y in range(2, 10))]

print(divisible_numbers)
