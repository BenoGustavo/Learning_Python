from time import sleep
from threading import Thread

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        print(f'Iniciando a thread: \n')
        for i in range(5):
            print(self.texto)
            sleep(self.tempo)
        print(f'{self.texto} finalizada')

if __name__ == "__main__":
    t1 = MeuThread('Thread 1', 2)
    t1.start()

    t2 = MeuThread('Thread 2', 2)
    t2.start()

    print("Thread comecou finalizada: \n")
    for i in range(20):
        print(i)
        sleep(1)