import random
from time import sleep
text = 'GAME IMPAR PAR'
print(f'\033[1;31;40m{text:^30}\033[m')
sleep(2)
print()
j = 0
v = 0
d = 0
l = random.randint(0,10)
while True:
    j += 1
    p = str(input('Esscolha entre imapar ou par?')).upper().strip()
    r = p[0]
    if r != 'I' and r != 'P':
        print('{}Valor errado{}'.format('\033[1;31m', '\033[m' ))
        p = str(input('Esscolha entre imapar ou par?')).upper().strip()
    print('-' * 20)
    nj = int(input('Digite seu números'))
    s = nj + l
    sleep(0.5)
    print(f'{l} + {nj} = {s}')
    numb = l + nj
    if r == 'P':
        if s % 2 == 0:
            print('Parabéns, você venceu !!')
            v += 1
        else:
            print('Você Perdeu !')
            d += 1
    if r == 'I':
        if s % 2 == 1:
            print('Parabéns, você venceu !!')
            v += 1
        else:
            print('Você Perdeu !')
            d += 1
    if r != 'I' and r != 'P':
        print('Valor errado')
    sleep(0.5)
    print('-'*20)
    print('\033[1;34mEstatisticas\033[m')
    print(f'Rodada {j}')
    print(f'Vitórias {v}')
    print(f'Derrotas {d}')
    print('-' * 20)
    sleep(1)


