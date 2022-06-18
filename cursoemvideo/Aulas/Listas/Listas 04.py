galera = list()
dado = dict()
totmai = totmen = 0

for c in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    galera.append({'nome': nome, 'idade': idade})
print()

for p in galera:
    if p.get('idade') >= 21:
        print(f"{p.get('nome')} é maior de idade.")
        totmai += 1
    else:
        print(f"{p.get('nome')} é menor de idade.")
        totmen += 1

print(f'\nTemos {totmai} maiores e {totmen} menores de idade.')
