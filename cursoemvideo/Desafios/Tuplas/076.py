itens = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
listagem = 'LISTAGEM DE PREÇO'
print('-' * 40)
print(f'{listagem:^40}')
print('-' * 40)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<31}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')
print('-' * 40)
