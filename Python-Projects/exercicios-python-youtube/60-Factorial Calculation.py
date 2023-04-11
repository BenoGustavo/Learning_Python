from math import factorial

while True:

    try:
        num = int(input("Insert a number to make the factorial: "))
        factorial_num = factorial(num)
        print(f"The factorial of {num} is {factorial_num}")
    
    except ValueError:
        print("Please, insert a valid value...")
        continue

