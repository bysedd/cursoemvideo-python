dinheiro = float(input('Quanto dinheiro você tem na sua carteira? \033[1;32mR$\033[m '))

print('Com \033[1;32mR${:.2f}\033[m você pode comprar \033[1;32mU${:.2f}\033[m'.format(dinheiro, dinheiro / 3.27))
