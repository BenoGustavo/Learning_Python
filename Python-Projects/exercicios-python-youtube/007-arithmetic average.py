qnt = int(input('How many numbers do you want? '))

x = 0
for i in range(qnt):
    grade = int(input('Enter the grade: '))

    x = (grade+x)

ArithmeticAverage = x/qnt

print('The arithmetic average is {}'.format(ArithmeticAverage))

