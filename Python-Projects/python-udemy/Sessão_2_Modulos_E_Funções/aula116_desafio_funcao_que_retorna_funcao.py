
def multiplicador(a):
    def multiplicar(numero):
        return numero * a
    return multiplicar


dobro = multiplicador(2)
triplo = multiplicador(3)
quadruplo = multiplicador(4)
quintuplu = multiplicador(5)

print(dobro(5))
print(triplo(5))
print(quadruplo(5))
print(quintuplu(5))
