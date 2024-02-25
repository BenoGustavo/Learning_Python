class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    #Sempre que a classe for instanciada ela vai retornar a mesma instancia.
    as1 = AppSettings()

    as1.tema = 'Qualquer outra coisa'

    as2 = AppSettings()
    as3 = AppSettings()

    print("Tema 1: ",end='')
    print(as1.tema)
    print("Tema 2: ",end='')
    print(as2.tema)
    print("Tema 3: ",end='')
    print(as3.tema)

    print("\nComparando as instancias:")
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)