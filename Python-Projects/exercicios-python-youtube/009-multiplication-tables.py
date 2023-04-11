x = int(input('Write the whished multiplication: '))

print('\n\n')

res = 0

y = x

count = 0
for i in range(11):
    res = x * count
    count = count + 1
    print('{} x {} = {}'.format(y,i,res))
    
