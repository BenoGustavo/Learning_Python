name = input("Write your full name: ").split(' ')

name_l = len(name)

print(f"Your first name is {name[0]}")
print(f"Your last name is {name[name_l-1]}")