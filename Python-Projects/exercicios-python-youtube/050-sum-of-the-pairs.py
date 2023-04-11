try:
    count = 0
    summed = 0
    for i in range(1,7):
        number = int(input(f"Insert the {i} number (only the pairs will be summed): "))
        if number % 2 == 0:
            summed += number
            count += 1

    print(f"You informed {count} pairs and the sum of all the numbers is {summed}")

except ValueError:
    print("\nPlease, insert a valid value...")