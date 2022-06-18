valores = []
pares = []
impares = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    resp = input('Quer continuar? [S/N] ').casefold()
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    if resp[0] == 'n':
        break
print('-=' * 30)
print(f'A lista completa é {valores}\n'
      f'A lista de pares é {pares}\n'
      f'A lista de ímpares é {impares}')
