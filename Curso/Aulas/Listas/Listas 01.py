num = [2, 5, 9, 1]  # LISTA
num[2] = 3  # ADICIONA 3 NA POSIÇÃO 2
num.append(7)  # ADICIONA 7 NA ÚLTIMA POSIÇÃO
num.sort(reverse=True)  # SORTEIO REVERSO
num.insert(2, 2)  # NA POSIÇÃO 2 ADICIONA 2
if 5 in num:  # SE TIVER 5 REMOVE
    num.remove(5)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos')  # CONTA OS ELEMENTOS DA VARIÁVEL
