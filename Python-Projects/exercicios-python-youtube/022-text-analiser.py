user_name = input('Write your full name: ')

print(f"\nYour name is {user_name}")
print(f"Your name in uppercase is {user_name.upper()}")
print(f"Your name in lowercase is {user_name.lower()}")
print(f"Your name have {len(user_name.replace(' ',''))} letters")

first_name = user_name.split()

print(f"Your first name have {len(first_name[1])} letters")
