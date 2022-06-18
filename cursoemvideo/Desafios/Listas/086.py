matriz = list()
for i in range(3):
    linha = list()
    for j in range(3):
        v = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(v)
    matriz.append(linha)
print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[\t{matriz[i][j]}\t]', end='')
    print()
