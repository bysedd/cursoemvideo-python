jogador = {'nome': input('Nome do jogador: '), 'gols': []}
n = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for p in range(n):
    jogador['gols'].append(int(input(f'   Quantos gols na partida {p + 1}? ')))
jogador['total'] = sum(jogador['gols'])
print(f"{'-=' * 30}\n{jogador}\n{'-=' * 30}")
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(f"{'-=' * 30}\nO jogador {jogador['nome']} jogou {n} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f"    => Na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")
