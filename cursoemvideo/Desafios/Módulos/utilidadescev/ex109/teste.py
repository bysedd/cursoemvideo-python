import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}\n'
      f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}\n'
      f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}\n'
      f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
