salário = float(input('Qual é o salário do funcionário? R$'))

if salário > 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, ((salário / 100) * 10) + salário))
if salário < 1250.00 or salário == 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, ((salário / 100) * 15) + salário))
