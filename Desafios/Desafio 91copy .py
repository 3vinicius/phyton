from random import randint
from time import sleep
from operator import itemgetter
bibli = {}
for c in range(1, 5):
    bibli[f'jogador{c}'] = randint(1, 6)
for k,v in bibli.items() :
    print(f'{k} tirou {v}')
    sleep(0.5)
print('RANKING')
ranking = sorted(bibli.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} ')