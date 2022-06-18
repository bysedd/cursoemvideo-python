print('\033[1;30m=\033[m' * 30)
print('          \033[1;36mBANCO CEV\033[m     ')
print('\033[1;30m=\033[m' * 30)

valor = int(input('\033[1;30mQue valor você quer sacar?\033[m \033[1;32mR$\033[m'))

total = valor
céd = 100
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'\033[1;30mTotal de {totcéd} cédulas de\033[m \033[1;32mR${céd}\033[m')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        totcéd = 0
        if total == 0 or total == 1:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
