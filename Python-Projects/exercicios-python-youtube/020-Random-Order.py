import random

num = int(input('How many studants do you want?: '))

list = []
for i in range(num):
    list.append(input(f'Insert the {i+1} studant: '))

random.shuffle(list)

print(f'The list shuffled list is {list}')