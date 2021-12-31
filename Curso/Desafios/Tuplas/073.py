classif = ('Atlético-MG', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Internacional', 'Fluminense', 'Grêmio',
           'Fortaleza', 'Corinthians', 'Athletico', 'Bahia', 'Atlético-GO', 'Bragantino', 'Ceará', 'Sport', 'Vasco',
           'Coritiba', 'Botafogo', 'Goiás')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {classif}')
print('-=' * 20)
print(f'Os 5 primeiros são {classif[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {classif[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfábetica: {sorted(classif)}')
print('-=' * 20)
print(f'O Flamengo está na {classif.index("Flamengo")+1}ª posição')
