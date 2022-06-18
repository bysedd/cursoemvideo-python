peso = float(input('Digite seu peso? (Kg) '))
altura = float(input('Digite sua altura? (m) '))

imc = peso / (altura * altura)

print('O IMC dessa pessoa é de \033[1;30m{:.1f}\033[m'.format(imc))

if imc < 18.5:
    print('Você está \033[31mABAIXO DO PESO\033[m normal.')
elif imc < 25:
    print('PARABÉNS, você está na faixa de \033[30mPESO NORMAL\033[m.')
elif imc < 30:
    print('Você está em \033[1;30mSOBREPESO\033[m, fique alerta!')
elif imc < 40:
    print('Você está em \033[31mOBESIDADE\033[m!')
else:
    print('Você está em \033[1;31mOBESIDADE MÓRBIDA\033[m, cuidado!')
