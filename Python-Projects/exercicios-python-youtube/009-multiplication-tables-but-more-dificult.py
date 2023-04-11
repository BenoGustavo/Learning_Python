x = int(input('Write the whished multiplication: '))
z = int(input('How many times do you want to multiply?: '))

print('\n\n')

res = 0

y = x

count = 0
for i in range(z+1):
    res = x * count
    count = count + 1
    print('{} x {} = {}'.format(y,i,res))
    
