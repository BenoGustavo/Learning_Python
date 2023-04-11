from os import system

while True:
    try:
        system("cls")
        term = int(input("Insert the quantity of terms: "))
        base = int(input("Insert the base: "))
        rate = int(input("Insert the rate: "))
        pa = base

        print(f"\nTerm [1] P.A = {pa}")
        for i in range(2,term+1):
            pa += rate
            print(f"Term [{i}] P.A = {pa}")

        print("\n")
        option = input("Do you want to leave? [y]es or type anything to continue: ")

        if option.lower()[0] == 'y':
            break
        else:
            continue

    except ValueError:
        print("\nPlease, insert a valid value\n")
        system("pause")
        continue