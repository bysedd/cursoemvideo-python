compras = float(input('Preço das compras: R$'))

print('\033[1;36m''-=-''\033[m' * 15)
print('''\033[1;30mFORMAS DE PAGAMENTO\033[m
\033[1;31m[ 1 ]\033[m à vista dinheiro/cheque - \033[1;30m10% DESCONTO\033[m
\033[1;32m[ 2 ]\033[m à vista no cartão - \033[1;30m5% DESCONTO\033[m
\033[1;33m[ 3 ]\033[m 2x no cartão - \033[1;30mSEM DESCONTO\033[m
\033[1;34m[ 4 ]\033[m 3x ou mais no cartão - \033[1;30m20% DE JUROS\033[m''')
print('\033[1;36m''-=-''\033[m' * 15)

desconto1 = compras * 0.10
desconto2 = compras * 0.05

opção = int(input('Qual é a opção? '))

if opção == 1:
    print('Sua compra de \033[1;32mR${:.2f}\033[m '.format(compras), end='')
    print('vai custar \033[1;32m{:.2f}\033[m no final.'.format(compras - desconto1))
elif opção == 2:
    print('Sua compra de \033[1;32mR${:.2f}\033[m '.format(compras), end='')
    print('vai custar \033[1;32mR${:.2f}\033[m no final.'.format(compras - desconto2))
elif opção == 3:
    print('Sua compra de \033[1;32mR${:.2f}\033[m '.format(compras), end='')
    print('vai custar \033[1;32mR${:.2f}\033[m no final.'.format(compras))
elif opção == 4:
    parcelado_em = int(input('Quantas parcelas? '))
    parcelas = (compras / parcelado_em) * 0.20
    parcelas_total = (compras / parcelado_em) + parcelas
    juros = (compras * 0.20) + compras
    print('Sua compra será parcelada em \033[1;30m{}x\033[m de \033[1;32mR${:.2f}\033[m COM JUROS'
          .format(parcelado_em, parcelas_total))
    print('Sua compra de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no final.'
          .format(compras, juros))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
