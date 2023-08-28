from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

#Abstração
class Log:
    def log(self,msg):
        raise NotImplementedError('Create the log method yourself')
    
    def log_error(self,msg):
        return self.log(f'Error:{msg}')
    
    def log_success(self,msg):
        return self.log(f'Success:{msg}') #Quando utilizado self. dentro de uma classe que ira sofrer herança a classe que herda deve ser a chamada
    
class LogFileMixin(Log):
    def log(self,msg):
        with open(LOG_FILE,'a') as arquivo:
            arquivo.write(msg)
            arquivo.write('\n')
        
    
class LogPrintMixin(Log):
    def log(self,msg):
        print(msg)

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Bom dia')
    lp.log_success('Bacana')

    lf = LogFileMixin()
    lf.log_success('banana')
    lf.log_error('ohhh no')