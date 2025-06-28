total_days = int(input(" Enter the number of days: "))
years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7

# print("Equivalence time is: ")
# print("years" , years)
# print("weeks" , weeks )
# print("days" , days)


print(f"Equivalent time is:\nYears={years}\nWeeks={weeks}\nDays={days}")