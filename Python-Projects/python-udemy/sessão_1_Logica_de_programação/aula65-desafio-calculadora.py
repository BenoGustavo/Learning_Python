while True:
    num1 = input("Insira o primeiro número: ")
    num2 = input("Insira o segundo número: ")
    Operador = input("Insira o operador número: ")

    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)

        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("\nInsira números validos")
        continue

    operador_valido = '+-/*'

    if Operador not in operador_valido:
        print("\nPor favor insira um operador valido")
        continue

    if len(Operador) > 1:
        print("\nInsira apenas um operador")
        continue

    if Operador == '+':
        resultado = num1_float + num2_float
        print(f"\nA soma dos valores é {resultado:.2f}")

    if Operador == '-':
        resultado = num1_float - num2_float
        print(f"\nA subtração dos valores é {resultado:.2f}")

    if Operador == '*':
        resultado = num1_float * num2_float
        print(f"\nA multiplicação dos valores é {resultado:.2f}")

    if Operador == '/':
        resultado = num1_float / num2_float
        print(f"\nA divisão dos valores é {resultado:.2f}")

    sair = input('\nQuer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
