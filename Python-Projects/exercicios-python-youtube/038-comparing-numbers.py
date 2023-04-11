first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

if int(first_number) == int(second_number):
    print(f"The numbers are equals {first_number} == {second_number}")

elif int(first_number) > int(second_number):
    print(f"The first numbers is greater then the second number {first_number} > {second_number}")

elif int(first_number) < int(second_number):
    print(f"The second numbers is greater then the first number {first_number} < {second_number}")

else:
    print("Não deveria chegar aqui")