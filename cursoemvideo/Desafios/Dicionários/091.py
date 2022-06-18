from random import randint
from time import sleep

d = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
c = 1
print('Valores sorteados:')
for k, v in d.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
sorted(d.values())
for i in sorted(d, key=d.get, reverse=True):
    print(f'   {c}º lugar: {i} com {d[i]}.')
    c += 1
    sleep(1)
