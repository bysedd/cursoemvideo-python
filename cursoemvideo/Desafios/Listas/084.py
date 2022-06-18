pessoas = list()
"""
Maria
70
s
João
100
s
Claudio
85
s
Hélio
100
s
Ana
70
s
Gustavo
80
n
"""
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append({'nome': nome, 'peso': peso})
    op = input('Quer continuar? [S/N] ').casefold()
    if op[0] == 'n':
        break
peso_maior = peso_menor = pessoas[0].get('peso')
for p in pessoas:
    if p.get('peso') > peso_maior:
        peso_maior = p.get('peso')
    if p.get('peso') < peso_menor:
        peso_menor = p.get('peso')
print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {peso_maior:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p.get('peso') == peso_maior:
        print(f"[{p.get('nome')}]", end=' ')
print(f'\nO menor peso foi de {peso_menor:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p.get('peso') == peso_menor:
        print(f"[{p.get('nome')}]", end=' ')
print()
