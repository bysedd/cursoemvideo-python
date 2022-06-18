n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O \033[1;30mPRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O \033[1;30mSEGUNDO\033[m valor é maior')
else:
    print('Os dois valor são \033[1;30mIGUAIS\033[m')
