import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}\n'
      f'O dobro de R${p} é R${moeda.dobro(p)}\n'
      f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}\n'
      f'Reduzindo 13%, temos R${moeda.diminuir(p, 13)}')
