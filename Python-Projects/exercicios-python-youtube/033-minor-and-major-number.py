def major_minor(*args):
    major=0
    minor=args[0]

    for numero in args:
        if numero > major:
            major = numero
        if numero < minor:
            minor = minor
    
    return f'The major number is {major} and the minor is {minor}'

number = major_minor(2,4,5,6,2,1,8,23,6)
print(number)

        