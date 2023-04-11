def grade_average(a,b,*args):
    average = a + b

    for number in args:
        average += number
    average = average/(len(args)+2)
    return average

average = grade_average(8,8,6,9)

if average >= 5 and average <= 6.9:
    print("Recuperação...")
elif average < 5:
    print("Reprovado...")
elif average >= 7:
    print("Aprovado...")