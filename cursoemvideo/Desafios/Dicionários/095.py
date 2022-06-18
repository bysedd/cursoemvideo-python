jogadores, c = [], 0
while True:
    print('-' * 40)
    jogador = {'cod': c, 'nome': input('Nome do jogador: ').title(), 'gols': []}
    n = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for p in range(n):
        jogador['gols'].append(int(input(f'\tQuantos gols na partida {p + 1}? ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)
    resp = input('Quer continuar? [S/N] ').upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break
    c += 1
print(f"{'-=' * 30}\n{'cod nome'}{'gols':>15}")
print('-' * 40)
for j in jogadores:
    print(f"{j['cod']:>3} {j['nome']:<15}{str(j['gols']):<14}")
while True:
    c = False
    busca = int(input('Mostrar dados de qual jogador? '))
    for j in jogadores:
        if j['cod'] == busca:
            print(f"-- LEVANTAMENTO DO JOGADOR {j['nome']}:")
            if len(j['gols']) == 0:
                print(f'   {j["nome"]} ainda não jogou nenhuma partida.')
            else:
                for i, g in enumerate(j['gols']):
                    print(f"   No jogo {i + 1} fez {g} gols.")
                print(f"Foi um total de {j['total']} gols.")
            print('-' * 40)
            c = True
        elif busca == -1:
            print(f"-- LEVANTAMENTO DO JOGADOR {j['nome']}:")
            if len(j['gols']) == 0:
                print(f'   {j["nome"]} ainda não jogou nenhuma partida.')
            else:
                for i, g in enumerate(j['gols']):
                    print(f"   No jogo {i + 1} fez {g} gols.")
                print(f"Foi um total de {j['total']} gols.")
            print('-' * 40)
            c = True
    if busca == 999:
        break
    if not c:
        print(f'\033[1:31mERRO! Não existe jogador com código {busca}!\033[m')
print('<< VOLTE SEMPRE >>')
