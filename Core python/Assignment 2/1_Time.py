# Convert the time entered in hh,min and sec into seconds.

H = int(input("Enter the number for hour: "))
min = int(input("Enter the number for min: "))
sec= int(input("Enter the number for sec:"))

total_sec = (H * 3600) + (min * 60) + sec

print("total_sec: ", total_sec)