número = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[1;32mBINÁRIO\033[m
[ 2 ] converter para \033[1;33mOCTAL\033[m
[ 3 ] converter para \033[1;34mHEXADECIMAL\033[m''')
print()

opção = int(input('Sua opção: '))

if opção == 1:
    print('\033[1;30m{}\033[m convertido para \033[1;32mBINÁRIO\033[m é igual a \033[1;30m{}\033[m'
          .format(número, bin(número)[2:]))
elif opção == 2:
    print('\033[1;30m{}\033[m convertido para \033[1;33mOCTAL\033[m é igual a \033[1;30m{}\033[m'
          .format(número, oct(número)[2:]))
elif opção == 3:
    print('\033[1;30m{}\033[m convertido para \033[1;34mHEXADECIMAL\033[m é igual a \033[1;30m{}\033[m'
          .format(número, hex(número)[2:]))
else:
    print('\033[1;31mERROR\033[m')
