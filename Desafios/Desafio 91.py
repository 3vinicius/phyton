from random import randint
from time import sleep
bibli = {}
list = []
for c in range(1,5):
    bibli['Jogador'] = c
    bibli['Valor'] = randint(1,6)
    list.append(bibli.copy())
    bibli.clear()
print('VALORES SORTEADOS')
print(bibli)
maior = 0
for b in range(0,4):
    print(f'O {list[b]["Jogador"]}° jogador tirou {list[b]["Valor"]}')
    sleep(0.5)
print()
print('RANKING')
print(list)

