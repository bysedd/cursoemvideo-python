soma = cont = 0
while True:
    num = int(input('Digite um valor \033[1;31m(999 para parar)\033[m: '))
    if num == 999:
        break
    soma += num
    cont += 1
print()
print(f'A soma dos \033[1;30m{cont}\033[m valores foi \033[1;32m{soma}!\033[m')
