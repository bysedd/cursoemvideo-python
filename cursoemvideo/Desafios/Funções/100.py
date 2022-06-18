from random import randint
from time import sleep


def sorteia(lista: list, n: int):
    print(f'Sorteando {n} valores da lista: ', end='')
    for i in range(n):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista: list):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {lista}, temos {s}')


numeros = list()
sorteia(numeros, 10)
somaPar(numeros)
