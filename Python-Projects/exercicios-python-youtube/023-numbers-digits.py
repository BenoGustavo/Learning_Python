numbers = input("Write a number between 1 and 1000: ")

if int(numbers) >= 1000 and int(numbers) <= 9999:

    print(f"thousand's: {numbers[0]}")
    print(f"hundred's: {numbers[1]}")
    print(f"dozen's: {numbers[2]}")
    print(f"units's: {numbers[3]}")

elif int(numbers) >= 100 and int(numbers) < 1000:

    print(f"hundred's: {numbers[0]}")
    print(f"dozen's: {numbers[1]}")
    print(f"units's: {numbers[2]}")

elif int(numbers) >= 10 and int(numbers) < 100:

    print(f"dozen's: {numbers[0]}")
    print(f"units's: {numbers[1]}")

elif int(numbers) > 0 and int(numbers) < 10:

    print(f"units's: {numbers[0]}")
else:
    print("Please, enter with a valid value")