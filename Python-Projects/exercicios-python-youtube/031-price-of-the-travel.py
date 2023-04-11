from os import system


while True:
    system("cls")

    travel = input("How long is your travel in km/h? || [quit] for quit: ")

    if travel.lower() == 'quit':
        break

    try:
        if int(travel) < 200 and int(travel) > 0:
            price = int(travel) * 0.50
            print(f"\nThe total price of your travel is {price}$\n")
            system("pause")
        else:
            price = int(travel) * 0.45
            print(f"\nThe total price of your travel is {price}$\n")
            system("pause")

    except ValueError:
        print("Please, enter a valid value")