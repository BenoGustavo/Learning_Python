"""
Contantes = "Variaveis" que não mudam e são escritas em letras maiusculas
Muitas condições no mesmo if é ruim
    <= Contagem de complexidade isso é ruim
"""

velocidade = 60
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    if (local_carro >= LOCAL_1 - RADAR_RANGE) and (local_carro <= LOCAL_1 + RADAR_RANGE):
        print("Seu carro foi multado")
    else:
        print("O carro não está passando no radar")
else:
    print("O carro não está acima da velocidade permitada")
