print('\033[1;30m''-=-''\033[m' * 10)
print('\033[1;34m''Analisador de Triângulos v2''\033[m')
print('\033[1;30m''-=-''\033[m' * 10)

print()

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

print()

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r3):
    print('Os segmento acima \033[1;32mPODEM FORMAR\033[m um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[1;30mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;30mESCALENO\033[m')
    else:
        print('\033[1;30mISÓSCELES\033[m')
else:
    print('Os segmento acima \033[1;31mNÃO PODEM FORMAR\033[m um triângulo.')
