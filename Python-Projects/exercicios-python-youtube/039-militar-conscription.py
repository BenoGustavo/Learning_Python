from datetime import date

year = date.today().year

born_year = input("Insert your born year: ")

try:
    conscription = year - int(born_year)

    if conscription > 18:
        time_to_make_the_conscription = ((int(born_year) + 18)-year)
        conscription_year = year - (time_to_make_the_conscription * -1)
        print(f"\nDo you need to make the conscription immediatly, you are {time_to_make_the_conscription * -1} years late\n")
        
        print(f"Your conscription was in {conscription_year}")
    elif conscription < 18:
        conscription_year = born_year + 18
        print(
            f"\nDon't worry about your conscription, is not the time already, but you need to make it in {time_to_make_the_conscription} year\n")
        print("it wiil be in {conscription_year}")
    elif conscription == 18:
        print(f"\n{year} is the perfect year to make your conscription\n")
    else:
        print("\nPlease, insert a valid value\n")
except ValueError:
    print("\nPlease, insert a valid value\n")
