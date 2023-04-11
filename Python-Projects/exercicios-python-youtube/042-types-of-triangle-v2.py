side_1 = input("Insert the first side: ")
side_2 = input("Insert the second side: ")
side_3 = input("Insert the third side: ")


try:
    equilatero = int(side_1) == int(side_2) and int(side_1) == int(side_3)
    isoceles = int(side_1) == int(side_2) or int(side_1) == int(side_3)
    escaleno = int(side_1) != int(side_2) and int(side_1) != int(side_3)

    can_make_a_triangle = int(side_1) < int(side_2) + int(side_3) and int(
        side_2) < int(side_1) + int(side_3) and int(side_3) < int(side_1) + int(side_2)

    if can_make_a_triangle:
        print("\nThis sides can make a triangle")
        if equilatero:
            print("\nAll the sides are equal, so you have a equilatero triangle")
        elif isoceles:
            print("\nTwo sides are equals so you have a isoceles triangle")
        elif escaleno:
            print(
                "\nYour triangle don't have any equal side, so it is a escaleno triangle")
    else:
        print("\nThis sides can't make a triangle")

except ValueError:
    print("Insert a valid value...")
