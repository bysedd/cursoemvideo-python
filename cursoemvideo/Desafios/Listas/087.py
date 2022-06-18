matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = soma_coluna3 = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
        if j == 2:
            soma_coluna3 += matriz[i][j]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.\n'
      f'A soma dos valores da terceira coluna é {soma_coluna3}.\n'
      f'O maior valor da segunda linha é {max(matriz[1])}.')
