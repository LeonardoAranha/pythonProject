import random
from time import sleep
num = random.randint(0, 5)
print('-=-' *16)
print('Tente advinhar em qual número estou pensando!!')
print('-=-' *16)
palp = int(input('Pra facilitar vou limitar os número de 0 a 5\nEntão, qual é o número? '))
print('-=-' *16)
if num == palp:
    print('PROCESSANDO...')
    sleep(2)
    print(f'Dessa vez você venceu ;-; , o número era {num}')
else:
    print('PROCESSANDO...')
    sleep(2)
    print('espera mais um pouco HEHE!')
    sleep(3)
    print(f'HAHA você errou!! o número era {num}. Mais sorte na proxima')
