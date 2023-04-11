from math import sqrt

CatOp = float(input('Insert the opposite cateto: '))
CatADJ = float(input('\nInsert the adjacent cateto: '))

Hip = CatOp**2 + CatADJ**2
Hip = sqrt(Hip)

print('\nThe hypotenuse is {}'.format(Hip))