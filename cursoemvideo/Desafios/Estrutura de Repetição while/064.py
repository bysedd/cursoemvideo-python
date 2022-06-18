flag = 999
num = 0
cont = 0
total = 0

while num != 999:
    num = int(input('\033[1;30mDigite um número\033[m \033[1;31m[999 para parar]\033[m: '))
    cont += 1
    total += num

print()
print('Você digitou \033[1;30m{} números\033[m e a soma entre eles foi \033[1;32m{}.\033[m'
      .format(cont - 1, total - 999))
