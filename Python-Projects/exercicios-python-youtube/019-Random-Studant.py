from random import choice


num = int(input('How many studants do you want to add to the list?: '))

list = []
for i in range(num):
    list.append(input(f'Insert the {i+1} studant: '))

chosen = random.choice(list)

print(f'The list is {list}')
print(f'And the chosen one is {chosen}')