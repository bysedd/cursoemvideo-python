def ficha(nome='', gol=''):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '' or not gol.isnumeric():
        gol = 0
    else:
        gol = int(gol)
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


print('-' * 30)
ficha(input('Nome do Jogador: '), input('Número de Gols: '))
