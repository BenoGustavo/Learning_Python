#!python

from math import pi
import sys


def circulo(raio):
    return pi * float(raio)**2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Informe o raio do circulo")
        print("Sintaxe: {} <raio>".format(sys.argv[0][-20:]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('área do círculo',area)

name = input('afdsa')