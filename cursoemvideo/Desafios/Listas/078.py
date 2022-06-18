valores = list()
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
    if valores == 1:
        maior = valores
        menor = valores
    else:
        if valores > maior:
            maior = valores
        if valores < menor:
            menor = valores
print('=-' * 30)
print(f'Você digitou os valores {valores}')
for c in enumerate(valores):
    print(f'O maior valor digitado foi {maior} nas posições {c}')
