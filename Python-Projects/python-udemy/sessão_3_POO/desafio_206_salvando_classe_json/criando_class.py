import json

CAMINHO = "json/base_dados.json"

class pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def get_idade(self):
        return self.idade

#Verificando se precisa salvar o arquivo
if __name__ == "__main__":
    p1= pessoa("Jorge","Matheus",12)
    p2= pessoa("Gustavo","Leandro",20)
    p3= pessoa("Duda","Bauer",19)

    banco_dados = [p1.__dict__,p2.__dict__,p3.__dict__]

    with open(CAMINHO,"w") as arquivo:
            json.dump(banco_dados,arquivo,indent=2,ensure_ascii=False)