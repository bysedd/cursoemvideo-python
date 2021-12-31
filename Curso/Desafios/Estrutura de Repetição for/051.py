print('\033[1;36m''=''\033[m' * 30)
print('     \033[1;30m10 TERMOS DE UMA P.A\033[m     ')
print('\033[1;36m''=''\033[m' * 30)

termo = int(input('\033[1;30mPrimeiro termo:\033[m '))
razão = int(input('\033[1;30mRazão:\033[m '))
décimo = termo + (10 - 1) * razão

for c in range(termo, décimo + razão, razão):
    print('\033[1;30m{}\033[m '.format(c), end='\033[1;32m->\033[m ')

print('\033[1;31mACABOU\033[m')
