import re


def leiaInt(msg):
    val = input(msg)
    while not (isinstance(val, int) or re.search(r'^-?\d+$', val)):
        print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        val = input(msg)
    return val


print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
