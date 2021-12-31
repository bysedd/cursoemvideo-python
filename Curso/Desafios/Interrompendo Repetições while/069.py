adulto = homens = mulheres = 0

while True:
    print('\033[1;30m-\033[m' * 25)
    print('   \033[1;36mCADASTRE UMA PESSOA\033[m   ')
    print('\033[1;30m-\033[m' * 25)
    idade = int(input('\033[1;34mIdade:\033[m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1;34mSexo: \033[m[\033[1;33mM\033[m/\033[1;35mF\033[m] ')).upper().strip()[0]
    if idade > 18:
        adulto += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    print('\033[1;30m-\033[m' * 25)
    continuar = str(input('\033[1;34mQuer continuar?\033[m [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()
    if continuar == 'N':
        print('\033[1;31m====== FIM DO PROGRAMA ======\033[m')
        break

print(f'\033[1;30mTotal de pessoas com mais de 18 anos: {adulto}\033[m')
print(f'\033[1;30mAo todo temos\033[m \033[1;34m{homens}\033[m \033[1;30mcadastrados\033[m')
print(f'\033[1;30mE temos\033[m \033[1;35m{mulheres}\033[m \033[1;30mmulheres com menos de 20 anos\033[m')
