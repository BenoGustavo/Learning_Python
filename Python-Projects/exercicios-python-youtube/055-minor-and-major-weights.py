try:
    bigger = 0.0
    minor = 0.0

    weights = int(input("How many weights do you want to compare: "))

    for num in range(1,weights+1):
        weight = float(input(f"Insert the {num} weight: "))
        
        if num == 1:
            minor = weight

        elif weight > bigger:

            bigger = weight
        elif weight < minor:

            minor = weight

    print(f"\nThe bigger weight is {bigger}")
    print(f"\nThe minor weight is {minor}")

except ValueError:
    print("Please, insert a valid value...")