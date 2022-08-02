from random import randint
list = []
lp = []
p = int(input('Quantos jogos voçê quer sortear'))
for c in range(1,p+1):
    for z in range(1,7):
        v = int(randint(1,60))
        while v in lp:
            v = int(randint(1, 60))
        lp.append(v)
    list.append(lp[:])
    lp.clear()
    print(f'{c}° jogo sorteado {list[c-1]}')


