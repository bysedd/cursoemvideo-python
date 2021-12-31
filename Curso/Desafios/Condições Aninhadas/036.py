from time import sleep

casa = float(input('Valor da casa: \033[1;32mR$\033[m '))
salário = float(input('Salário do comprador: \033[1;32mR$\033[m '))
anos = int(input('Quantos anos de financiamento? '))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print()
print('Para pagar uma casa de \033[1;32mR${:.2f}\033[m '
      'em \033[1;30m{}\033[m anos '
      'a prestação será de \033[1;32mR${:.2f}\033[m'
      .format(casa, anos, prestação))
print()
print('\033[1;35mAnalisando Dados...\033[m')
sleep(2)
print()

if prestação >= mínimo:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')
else:
    print('\033[1;32mEmpréstimo CONCEDIDO!\033[m')
