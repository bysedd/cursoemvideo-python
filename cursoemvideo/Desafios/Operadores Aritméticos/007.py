num1 = float(input('Primeira nota do aluno: '))
num2 = float(input('Segunda nota do aluno: '))

print('A média entre \033[1;30m{}\033[m e \033[1;30m{}\033[m é igual a \033[1;7;30;31m{:.1f}\033[m'
      .format(num1, num2, (num1 + num2) / 2))
