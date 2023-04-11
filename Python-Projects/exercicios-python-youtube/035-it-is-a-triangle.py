from os import system

while True:

    system("cls")
    print("Triangle analiser || [quit] to break\n")

    r1 = input("First segment: ")
    r2 = input("Second segment: ")
    r3 = input("Third segment: ")

    if r1.lower() == 'quit' or r2.lower() == 'quit' or r3.lower() == 'quit':
        break

    if int(r1) < int(r2) + int(r3) and int(r2) < int(r1) + int(r3) and int(r3) < int(r1) + int(r2):
        print("\nOs segmentos PODEM formar um triangulo.\n")
    else:
        print("\nOs segmentos NÃO formam um triangulo.\n")

    system("pause")