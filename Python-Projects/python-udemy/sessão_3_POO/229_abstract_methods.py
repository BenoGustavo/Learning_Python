from abc import ABC,abstractclassmethod

#Abstração
class Log(ABC): #Diz para o python q essa classe é abstrata
    
    @abstractclassmethod
    def log(self,msg): ...
        #raise NotImplementedError('Create the log method yourself')
    
    def log_error(self,msg):
        return self.log(f'Error:{msg}')
    
    def log_success(self,msg):
        return self.log(f'Success:{msg}') #Quando utilizado self. dentro de uma classe que ira sofrer herança a classe que herda deve ser a chamada


class LogPrintMixin(Log):
    def log(self,msg):
        print(msg)

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('oi')