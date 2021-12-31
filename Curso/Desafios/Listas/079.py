lista = list()
resp = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor != lista:
        print('Valor adicionado com sucesso...')
        lista.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('=-' * 25)
print(f'Você digitou os valores {lista.sort}')
