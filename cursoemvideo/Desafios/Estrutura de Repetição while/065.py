resp = 'S'
soma = quant = média = maior = menor = 0

while resp == 'S':
    numero = int(input('\033[1;30mDigite um número:\033[m '))
    resp = str(input('\033[1;36mQuer continuar?\033[m [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).strip().upper()
    quant += 1
    soma += numero
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
média = soma / quant
print('Você digitou \033[1;30m{} números\033[m e a\033[1;32m média foi {:.2f}\033[m'.format(quant, média))
print('O\033[1;30m maior valor foi {}\033[m e o \033[1;30mmenor foi {}\033[m'.format(maior, menor))
