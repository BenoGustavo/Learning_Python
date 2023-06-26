#Criando a classe pessoa
class pessoa:
    #Constructor
    def __init__(self,nome,idade,genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    #coloca um valor em genero sem utilizar o __init__
    def set_genero(self,genero):
        self.genero = genero

    #Retorna o valor de genero (se existir retornar o genero se não retorna zero)
    def return_genero(self,genero):
        if self.genero:
            return self.genero
        return 0