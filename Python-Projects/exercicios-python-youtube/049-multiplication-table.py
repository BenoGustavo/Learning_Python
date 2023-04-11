try:
    multiple = float(input("Insert the number that you want to see the multiplication table: "))
    times = int(input("How many time do you want to multiply: "))
    
    print("\n")

    for i in range (times+1):
        print(f"{i} x {multiple} = {multiple*i}")

except ValueError:
    print("\nPlease, insert a valid value...")
