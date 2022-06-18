from random import randint
from time import sleep

print(f"{'-' * 30}\n\t\t  MEGA SENA\n{'-' * 30}")
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f"{'-=' * 3}SORTEANDO {n} JOGOS  {'-=' * 3}")
for c in range(n):
    cartela = list()
    while len(cartela) < 6:
        numero = randint(1, 60)
        if numero not in cartela:
            cartela.append(numero)
    print(f'Jogo {c + 1}: {sorted(cartela)}')
    sleep(1)
print(f"{'-=' * 5} < BOA SORTE! > {'-=' * 5}")
