try:
    base = int(input("Insert the base of the A.P: "))
    ratio = int(input("Insert the ratio of the A.P: "))
    times = int(input("How many values do you want? "))
    ap = base
    count = 1

    while count != times+1:
        print(f"The [{count}] number of the ap is [{ap}]")
        ap += ratio

        count += 1

except ValueError:
    print("Please, insert a valid value...")