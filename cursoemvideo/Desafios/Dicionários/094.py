# Lendo os dados
grupo, media, c = [], 0, 0
while True:
    nome = input('Nome: ').title()
    sexo = input('Sexo: [M/F] ').upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = input('Sexo: [M/F] ').upper()[0]
    idade = int(input('Idade: '))
    media += idade
    grupo.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    resp = input('Quer continuar? [S/N] ').upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO! Responda apenas S ou N.')
        resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break
# Analisando os dados e mostrando o resultado final
print(f"{'-=' * 30}\nA) Ao todo temos {len(grupo)} pessoas cadastradas.")
media //= len(grupo)
print(f"B) A média de idade é de {media} anos.")
print('C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p.get('sexo') == 'F':
        print(f"[{p.get('nome')}]", end=' ')
        c += 1
if c == 0:
    print('[]', end='')
    c = 0
print(f"\nD) Lista de pessoas que estão acima da média:")
for p in grupo:
    if p.get('idade') >= media:
        print(f"\tnome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}.")
        c += 1
if c == 0:
    print('\tNenhuma pessoa acima da média.')
print(f"<< ENCERRADO >>")
