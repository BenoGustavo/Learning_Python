from os import system
from time import sleep

val_1 = int(input("Insert the first number: "))
val_2 = int(input("Insert the second number: "))

while True:
    try:
        system("cls")

        print("Menu: What do you want to do...")
        print("[ 1 ] - Sum")
        print("[ 2 ] - Multiply")
        print("[ 3 ] - Biggest")
        print("[ 4 ] - New Numbers")
        print("[ 5 ] - Leave\n")

        op = int(input("Type the option that you want: "))

        if op == 1:
            val_sum = val_1 + val_2
            print(f"\nThe sum of the values are {val_sum}\n")
            sleep(2)
            continue

        elif op == 2:
            val_mul = val_1 * val_2
            print(f"\nThe multiplication of the values are {val_mul}\n")
            sleep(2)
            continue

        elif op == 3:
            if val_1 > val_2:
                print(f"\nThe biggest value is {val_1}\n")
                sleep(2)
            else:
                print(f"\nThe biggest value is {val_1}\n")
                sleep(2)
                continue

        elif op == 4:
            val_1 = int(input("\nInsert the first number: "))
            val_2 = int(input("Insert the second number: "))
            continue

        elif op == 5:
            break

        else:
            print("\nInsert a valid value...\n")
            sleep(2)
            continue

    except ValueError:
        print("\nPlease, insert a valid number\n")
        sleep(2)
        continue
