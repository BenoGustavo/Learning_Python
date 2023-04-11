try:
    count = 0
    check_integer_number = 0

    numbers = int(input("Insert the number to know if it is cousin: "))

    for num in range(1,numbers+1):

        check_integer_number = (numbers/num)

        if check_integer_number.is_integer():
            print(f"\nThe number {num} is divisible by {numbers} ")
            count += 1

        else:
            print(f"\nThe number {num} is not divisible by {numbers} ")

    if count == 2:
        print(f"\nThe number {numbers} is a cousin number...\n")
    else:
        print(f"\nThe number {numbers} is not a cousin number, it was divisible {count} times...\n")

except ValueError:
    print('\nPlease, insert a valid value...')