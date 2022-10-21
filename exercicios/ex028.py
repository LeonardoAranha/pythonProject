import random
from time import sleep
num = random.randint(0, 5)
print('\033[33m-=-\033[m' *16)
print('\033[31mTente advinhar em qual número estou pensando!!\033[m')
print('\033[33m-=-\033[m' *16)
palp = int(input('\033[31mPra facilitar vou limitar os número de 0 a 5\nEntão, qual é o '
                 'número? \033[m'))
print('\033[33m-=-\033[m' *16)
if num == palp:
    print('\033[30;107mPROCESSANDO...\033[m')
    sleep(2)
    print(f'\n\033[36mDessa vez você venceu ;-; , o número era {num}\033[m')
else:
    print('\033[30;107mPROCESSANDO...\033[m')
    sleep(2)
    print('\n\033[31mespera mais um pouco HEHE!\033[m')
    sleep(3)
    print(f'\n\033[31mHAHA você errou!! o número era {num}. Mais sorte na proxima\033[m')
