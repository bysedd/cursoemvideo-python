frase = str(input('Digite uma frase: ')).strip().upper()

separa = frase.split()
junta = ''.join(separa)
inverso = ''

for c in range(len(junta) - 1, -1, -1):
    inverso += junta[c]

print('O inverso de \033[30m{}\033[m é \033[1;30m{}\033[m'.format(junta, inverso))

if inverso == junta:
    print('\033[1;32mTemos\033[m um \033[1;30mpalíndromo!\033[m')
else:
    print('A frase digitada \033[1;31mnão\033[m é \033[30mpalíndromo!\033[m')
