somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

totpessoas = int(input('Quantas pessoas? '))

for pessoa in range(1, totpessoas + 1):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / totpessoas

print()
print('A média de idade do grupo é de \033[1;30m{:.0f} anos.\033[m'
      .format(médiaidade))
print('O homem mais velho tem \033[1;30m{} anos\033[m e se chama \033[1;30m{}.\033[m'
      .format(maioridadehomem, nomevelho))
print('Ao todo são \033[1;35m{} mulher(es)\033[m com menos de \033[1;30m20 anos.\033[m'
      .format(totmulher20))
