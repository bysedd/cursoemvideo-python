dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

total_dias = dias * 60
total_km = km * 0.15
total = total_dias + total_km

print('O total a pagar é de \033[1;32mR${:.2f}\033[m'.format(total))
