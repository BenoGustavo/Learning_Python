end_num = 0
count = 0
sum_num = 0
num = 0

try:
    while int(end_num) != 999:
        sum_num += num
        count += 1

        num = int(input("What number do you want? (999 to end): "))

        end_num = num
    print(f"\nDo you wrote {count-1} numbers, and the sum of them is {sum_num}")

except ValueError:
    print("\nPlease, enter a valid value...")
