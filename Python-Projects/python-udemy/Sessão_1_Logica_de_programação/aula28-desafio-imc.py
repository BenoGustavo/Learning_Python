nome = input("Insira seu nome: ")
altura = float(input("Insira sua altura em metros: "))
peso = int(input("Insira seu peso: "))
imc = (peso / (altura**2))

print(f"O senhor(a) {nome} tem o IMC de {imc:.2f}")
