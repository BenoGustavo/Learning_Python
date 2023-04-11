from datetime import date

today_year = date.today().year

try:
    major_age = 0
    minor_age = 0

    people_list = []

    peoples = int(input("How many people do you want to know the age? "))

    for people_num in range(1,peoples+1):
        birthyear = int(input(f"Type the birth date of the {people_num}: "))

        age = today_year - birthyear

        if age >= 18:
            people_list.append(f"\nThe {people_num} people is older aged, with {age} years")
            major_age += 1
        else:
            people_list.append(f"\nThe {people_num} people is underage, with {age} years")
            minor_age += 1

    for people_num in range(0,peoples):
        print(f"{people_list[people_num]}")
    print(f"\n{minor_age} is underage and {major_age} is older age")

except ValueError:
    print("\nPlease, insert a valid value...")