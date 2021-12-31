while True:
    valor = int(input('\033[1;36mQuer ver a tabuada de qual valor?\033[m '))
    print('\033[1;30m---\033[m' * 12)
    if valor <= -1:
        break
    for vezes in range(1, 11):
        mult = valor * vezes
        print(f'{valor} x {vezes} = {mult}')
    print('\033[1;30m---\033[m' * 12)
print('\033[1;31mPROGRAMA TABUADA ENCERRADO\033[m. \033[1;30mVolte sempre!\033[m')
