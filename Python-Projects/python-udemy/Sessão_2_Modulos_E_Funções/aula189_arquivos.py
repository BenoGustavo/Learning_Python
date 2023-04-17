from time import sleep
import os

caminho = 'arquivo_python.txt'

# W pois apenas posso escrever, com W+ posso escrever e ler, 
# porém se um arquivo já existir apaga tudo q tem la dentro, 
# para manter e concatenar utilize o metodo a

#enconding utf8 especifica os tipos de caracteres utilizados, permitindo ç ~

with open(caminho, 'w', encoding='utf8') as arquivo_txt: 
    arquivo_txt.write("Escrevendo uma linha\n\n")
    
    arquivo_txt.writelines(
        ["Atenção\n",
         "Estou\n",
        "Escrevendo\n",
         "Varias\n",
         "Linhas\n",
         "Em\n",
         "Um\n",
         "Comando\n"
         ]
    )

with open(caminho, 'r') as arquivo_txt: #R pois apenas posso ler
    print(arquivo_txt.read()) #Le o arquivo completo
    print(arquivo_txt.readline()) #Le apenas uma linha

    print('\nApagando o arquivo em:')

print("Vou trocar de nome...\n")
sleep(1)

os.rename(caminho,'troquei_de_nome.txt')

for segundo in range(1,6):
    sleep(1)
    print(segundo)

os.remove('troquei_de_nome.txt') #Deleta o arquivo