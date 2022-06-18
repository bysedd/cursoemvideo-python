maior = 0
menor = 0

vezes = int(input('Quantas pessoas? '))

for pessoa in range(1, vezes + 1):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print()
print('O \033[1;31mmaior\033[m peso lido foi de \033[1;30m{}\033[m\033[30m Kg\033[m'.format(maior))
print('O \033[1;32mmenor\033[m peso lido foi de \033[1;30m{}\033[m\033[30m Kg\033[m'.format(menor))
