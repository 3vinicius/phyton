## Import
from time import sleep


## Progamas
def maior(*a):
    print('-='*25)
    print('Analizando os valores.......')
    m = 0
    for v in a:
        for n in v:
            if n >= m:
                sleep(0.5)
                m = n
                print(f'{n}', end=' ', flush=True)
    sleep(0.5)
    print(f'Foram analizado {len(a)} valores ao todo')
    sleep(0.5)
    print(f'O maior valor é {m}')


l = [2, 3, 4, 6, 7, 8, 2, 5, 7, 10, 4, 3, 23, 5, 2, 0, 1]
maior(l)
maior([0])
maior([2,4,5,6,7,3,4,1,34,5,634,0])