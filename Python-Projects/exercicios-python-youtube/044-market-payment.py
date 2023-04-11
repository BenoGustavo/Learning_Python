
from os import system


while True:
    system("cls")
    try:
        price_of_the_purcharses = float(input("How much do you will pay? "))
        print("\nMenu:\n[1] - Pay in cash || check\n[2] - Pay in installments\n[3] - Leave\n")
        option = int(input("Choose a option: "))

        if option == 3:
            break

        if option == 1:
            price_with_discount = price_of_the_purcharses * 0.10
            price_with_discount -= price_of_the_purcharses

            print(f"\nYou received a discount || Your buy {price_of_the_purcharses}R$ || Your buy after the 10% discount {price_with_discount*-1}R$")
        
        elif option == 2:
            option = int(input("How many installments do you want?: "))
            
            if option == 1:
                price_with_discount = price_of_the_purcharses * 0.05
                price_with_discount -= price_of_the_purcharses

                print(f"\nSo, you will pay with discount {price_with_discount*-1}R$ || Total {price_of_the_purcharses}R$")
            elif option == 2:
                print(f"So, you will pay {price_of_the_purcharses/2}R$ per month || Total {price_of_the_purcharses}R$")
            elif option > 2:
                price_with_FEES = price_of_the_purcharses * 0.20
                price_with_FEES += price_of_the_purcharses

                print(f"So, you will pay {price_with_FEES/option}R$ per month || Total {price_with_FEES}R$")
            else:
                print("Insert a valid value...")

        print("\n")
        option = input("Buy something else? [y]es or [n]o")

        if option[0].lower == 'y':
            continue
        elif option[0].lower == 'n':
            break


    except ValueError:
        print("\nPlease, insert a valid value...\n")
        system("pause")
        continue