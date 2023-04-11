import calendar
from datetime import date
from os import system

while True:

    system("cls")

    year = input("What's your year || type: [quit] to leave: ")

    if year.lower() == 'quit':
        break

    if year == '':
        year = date.today().year

    try:
        if calendar.isleap(int(year)):
            print(f"\nThe year {year} is a leap year.\n")
            system("pause")
        else:
            print(f"\nThe year {year} isn't a leap year.\n")
            system("pause")

    except TypeError:
        print("\nPlease, enter a valid value\n")

