try:
    peoples = {}
    age_stack = 0
    above_twenty = 0
    older_men = 0
    older_men_name = ""
    men = 0

    how_many = int(input("How many peoples do you want to analyze: "))

    for i in range(1, how_many+1):
        print(f"\n-=-=-=-=-People N{i}°-=-=-=-=-")
        name = input(f"Insert the name of the {i}° people: ")
        age = int(input(f"Insert the age of the {i}° people: "))
        sex = input(f"Insert the sex of the {i}° people [F OR M]: ")

        age_stack += age

        if sex.upper() == "M":
            if age > older_men:
                older_men_name = name
                older_men = age

        if sex.upper() == "F" and age < 20:
            above_twenty += 1

        if sex.upper() != 'M' and sex.upper() != "F":
            print("Please, enter a valid sex...")
            i = i - 1
            continue

        peoples[i] = {f"People [{i}]": {"Name": {name.capitalize()}, "Age": {
            age}, "Sex": {sex}}}

    for i in range(1, how_many+1):
        print(peoples[i], sep=" ")


except ValueError:
    print("Please, insert a valid value...")
