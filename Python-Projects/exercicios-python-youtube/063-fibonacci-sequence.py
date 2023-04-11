try:
    fibonacci = 0

    terms = int(input("How many terms do you want to see: "))

    print("\n")
    while terms != 0:
        fibonacci = fibonacci-1 + fibonacci-2

        print(f"{fibonacci}",end="")

        terms -= 1

except ValueError:
    print("Please, insert a valid value...")