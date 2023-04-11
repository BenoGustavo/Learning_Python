from datetime import date

year = date.today().year

born_year = input("Insert your year of birth: ")

try:
    actual_age = year - int(born_year)

    if actual_age > 0 and actual_age <= 9:
        print("\nYou are a mirim swimmer")
    elif actual_age > 9 and actual_age <= 14:
        print("\nYou are a infant swimmer")

    elif actual_age > 14 and actual_age <= 19:
        print("\nYou are a junior swimmer")

    elif actual_age > 19 and actual_age <= 25:
        print("\nYou are a senior swimmer")

    elif actual_age > 25:
        print("\nYou are a MASTER swimmer")
    else:
        print("\nA child without at least one year don't swim")
except ValueError:
    print("\nInsert a valid value...")
