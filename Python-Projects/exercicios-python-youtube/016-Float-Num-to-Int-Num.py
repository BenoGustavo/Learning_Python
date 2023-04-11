num = float(input('Insert the number that you want to break: '))

numdec = num
numdec = numdec - int(num)

print('\nThe number {} has the integer value of {} and {:.2f} floating\n'.format(num,int(num),numdec))