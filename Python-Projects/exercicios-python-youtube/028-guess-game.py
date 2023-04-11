from random import randint
from time import sleep
from os import system

while True:
    system("cls")

    print("Try to guess what im thinking, it is a number between 0 and 5 || [Leave] to give up\n")
    guess = input("Your guess is: ")

    if guess.lower() == 'leave':
        break

    number = randint(0, 5)

    print("Thinking...")
    sleep(2)

    try:

        if int(guess) >= 0 and int(guess) <= 5:
            if guess == str(number):
                print(
                    f"\nCongratulations, you guessed right, the number i was thing was {number}")
            else:
                print(
                    f"\nMore luck next time, you guessed wrong, the number i was thing was {number}")
        else:
            print("\nHey dude, try to follow the rules ok?")

        system("pause")

    except ValueError:
        print("\nHey dude, try to follow the rules ok?")

        system("pause")
