from os import system
from random import randint

times = 1

machine = randint(0,10)

try: 
    system("cls")
    
    print("Hello, im your computer...")
    print("Ï'm thinking in a number between 0 and 10.")
    print("Can you guess the number that i'm thinking?")
    guess = int(input("What's your guess? "))

    while guess != machine:
        system("cls")

        if guess < machine:
            print("Guessed wrong, it's a higher numbers, try again...")

        elif guess > machine:
            print("Guessed wrong, it's a lower numbers, try again...")
        
        guess = int(input("What's your guess? "))

        times += 1


    if guess == machine:
        print(f"\nYou guessed right, im thinking in {machine}, you guessed wrong {times} times")

except ValueError:
    print("Please, insert a valid value...")