name = input("Write your name: ").lower().split()

print('Your name have silva ?')

flag = 0

for part_of_the_name in name:
    if part_of_the_name == 'silva':
        print('silva' in name )
        flag += 1

if flag == 0:
    print(False)