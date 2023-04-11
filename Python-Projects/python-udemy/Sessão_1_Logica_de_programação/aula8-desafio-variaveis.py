nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
ano_de_nascimento = 2022 - idade
maior_de_idade = idade >= 18
altura = float(input("Digite sua altura: "))

print("\n\nNome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_de_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura)