n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

média = (n1 + n2) / 2

print('Tirando \033[1;30m{}\033[m e \033[1;30m{}\033[m, a média do aluno é \033[1;30m{:.1f}\033[m'
      .format(n1, n2, média))

if média < 5.0:
    print('O aluno está \033[1;31mREPROVADO\033[m')
elif média > 7.0:
    print('O aluno está \033[1;32mAPROVADO\033[m')
else:
    print('O aluno está em \033[1;33mRECUPERAÇÃO\033[m')
