from os import system

while True:
        
    system("cls")

    velocity = input("Insert the how many KM per H you are || [Quit] to leave: ")

    if velocity.lower() == 'quit':
        break

    try:
        if int(velocity) > 80:
            multa = (int(velocity) - 80) * 7
            print(f"\nYou were above the allowed velocity [ 80km/h ]: Pay [{multa}$]\n")

            system("pause")
        else:
            print(f"\nYou were down the allowed velocity [ 80km/h ]: you don't need to pay anything\n")

            system("pause")

    except ValueError:
        print("Please, insert a valid value...")