sum_of_numbers = 0
count_odd = 0

for i in range(0,501,3):
    
    if i % 2 == 0:
        continue
    else:
        sum_of_numbers += i
        count_odd += 1

print(f"There is {count_odd} odds numbers and the sum of them all is {sum_of_numbers}")