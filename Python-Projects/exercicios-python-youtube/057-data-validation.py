sex = input("Type your gender [M/F]: ").replace(' ','').upper()[0]
while sex not in 'MF':
    sex = input("Insert a valid algument. Type your gender [M/F]: ").replace(' ','').upper()[0]
    if sex in 'MF':
        print("\nSex collected with sucess\n")

print(f'Your sex is {sex}')