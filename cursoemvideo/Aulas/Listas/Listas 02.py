valores = list()
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
print()
for c, v in enumerate(valores):
    print(f'Na posição {c + 1} encontrei o valor {v}!')
print()
print('Cheguei ao final da lista.')
