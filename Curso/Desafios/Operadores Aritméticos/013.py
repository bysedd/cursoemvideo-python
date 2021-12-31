salário = float(input('Qual é o salário do Funcionário? \033[1;32mR$\033[m '))

aumento = (salário / 100) * 15
novo_salario = salário + aumento

print('Um funcionário que ganhava \033[1;32mR${}\033[m, com 15% de aumento,'
      ' passa a receber \033[7;1;32mR${:.2f}\033[m'
      .format(salário, novo_salario))
