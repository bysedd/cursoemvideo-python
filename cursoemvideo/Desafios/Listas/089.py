classe = list()

i = 0
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    classe.append({
        'id': i,
        'nome': nome,
        'notas': [nota1, nota2],
        'media': media
    })
    resp = input('Quer continuar? [S/N] ').casefold()
    if resp == 'n':
        break
    else:
        i += 1
print(f"{'-=' * 40}\n{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}\n{'-' * 35}")
for aluno in classe:
    print(f"{aluno.get('id'):<4}{aluno.get('nome'):<10}{aluno.get('media'):>8.1f}")
while True:
    print('-' * 50)
    resp, p = int(input('Mostrar notas de qual aluno? (999 interrompe): ')), ''
    if resp == 999:
        break
    else:
        for aluno in classe:
            if aluno.get('id') == resp:
                p = f"Notas de {aluno.get('nome')} são {aluno.get('notas')}"
                print(p)
        if p == '':
            print('\033[1:31mID não encontrado!\033[m')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
