
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter any Number for x:"))
n  = int(input("Enter any Number for n:"))

sum = x

ntr, dtr = 1, 1
for _ in range(2, n+1):
    ntr = ntr + 1
    dtr = dtr + 2
    temp_sum = x * ntr / dtr
    
    if ntr % 2 == 0:
        sum -= temp_sum
    else:
        sum += temp_sum
        
print(f"Sum = {sum}")

    
    