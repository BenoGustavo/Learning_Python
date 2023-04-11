number = input("Enter a integer number: ")

print("[1] - Binary\n[2] - Octal\n[3] - Hex")
op = input("\nChoose a option: ")

if op == '1':
    print(f"\nThe binary of {number} is {bin(int(number))[2:]}")
elif op == "2":
    print(f"\nThe octal of {number} is {oct(int(number))[2:]}")
elif op == '3':
    print(f"\nThe hex of {number} is {hex(int(number))[2:]}")
else:
    print("\nPlease, enter with a valid value")