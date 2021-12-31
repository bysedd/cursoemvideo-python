from datetime import date

nascimento = int(input('Ano de nascimento: '))

ano = date.today().year
idade = ano - nascimento

print('O atleta tem \033[1;30m{} anos\033[m.'.format(idade))

if idade < 9:
    print('Classificação: \033[1;31mMIRIM\033[m')
elif idade < 14:
    print('Classificação: \033[1;32mINFANTIL\033[m')
elif idade < 19:
    print('Classificação: \033[1;33mJUNIOR\033[m')
elif idade < 25:
    print('Classificação: \033[1;34mSÊNIOR\033[m')
else:
    print('Classificação: \033[1;35mMASTER\033[m')
