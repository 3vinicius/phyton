from time import sleep
import pygame


pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(10)
pygame.mixer.music.play()




bb = {}
gols = []
jogador = []
#jogador = [{'nome': 'Neymar', 'gols': [0, 0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 0]}, {'nome': 'Ronaldo', 'gols': [2, 3, 1, 0, 1, 2, 1, 4, 3]}, {'nome': 'Vini', 'gols': [2, 1, 3, 0, 1, 1, 0, 2, 0, 1, 0, 0, 1, 0, 2, 1]}, {'nome': 'Ewerton', 'gols': [2, 1, 3, 0, 1, 1, 0, 2, 0]}, {'nome': 'Lucas', 'gols': [1, 4, 3]}, {'nome': 'Jose', 'gols': [3, 1, 0, 1, 2, 1, 4, 3]}, {'nome': 'Rafael', 'gols': [2, 1, 3, 0, 1, 1, 0,]}, {'nome': 'Carlos', 'gols': [1, 0, 1, 2, 1, 4, 3]}, {'nome': 'Kaka', 'gols': [1, 2, 4, 0, 0, 2, 3, 1, 0, 1, 2, 1, 4, 3]}, {'nome': 'Murilo', 'gols': [2, 2, 1, 4, 3]}]

while True:
    print(f'\033[1;30;42m{"-NOVO CADASTRO -":=^80}\033[m')
    print()
    sleep(0.5)
    bb['nome'] = input("Digite o nome do jogador: ").capitalize()
    p = int(input('Quantas partidas ele jogou ? '))
    for q in range(1,p+1):
        g = int(input(f'Quantos gols ele fez na {q}° partida?'))
        while True:
            if g >=0:
                break
            g = int(input(f'Quantos gols ele fez na {q}° partida?'))
        gols.append(g)
    bb['gols'] = gols
    jogador.append(bb.copy())
    gols.clear()
    bb.clear()
    perg = input("Deseja realizar um novo cadastro? [Sim/Não] ").upper()
    while True:
        if perg[0] in "SN":
            break
        perg = input('Deseja realizar um novo cadastro ? Responda "Sim" ou "Não". ').upper()
    if perg[0] in 'N':
        break
print()
print(f'\033[1;31m{"=>ESTATISTICAS<=":=^80}\033[m')
print()
sleep(0.5)
s = 0
print(f'\033[1mN°     Nome       Gols:                                       Total:\033[m')
for b in jogador:
    sleep(0.3)
    print(f'{s:<}   {b["nome"]:<10}   {str(b["gols"]):<50} {sum(b["gols"]):<}')
    s += 1
sleep(0.5)
print(f'\033[1;31m{"="*80}\033[m')
while True:
    ind = int(input('Deseja Ver as estatisticas de qual jogador ?'))
    sleep(0.2)
    while True:
        if 0<= ind <=s:
            break
        ind = str(input(f'Digite o N° do jogador entre 0 e {s} para ver suas estastitisticas'))
        print(f'\033[1mN°  Nome:     Total:\033[m')
        N = 0
        for b in jogador:
            sleep(0.3)
            print(f'{N}   {b["nome"]:10}    {sum(b["gols"]):>}')
            N += 1
        sleep(0.5)
        print(f'\033[1;31m{"=" * 80}\033[m')
    ind = int(ind)
    b = jogador[ind]
    l = b['gols']
    for n,g in enumerate(l):
        sleep(0.2)
        print(f'Na partida {n}, {b["nome"]} fez {g}')
    print(f'Total {sum(b["gols"])}')
    print(f'\033[1;31m{"="*80}\033[m')
    ot = input("Deseja ver outro jogador? [SIM/NÃO]").upper()
    while True:
        if ot[0] in "SN":
            break
        ot = input('Digite "Sim" ou "Não" se deseja ver a estatistica de outra jogador " ')
    if ot[0] in "N":
        break
    N = 0
    sleep(0.5)
    print(f'\033[1;31m{"=" * 80}\033[m')
    print(f'\033[1mN°  Nome:     Total:\033[m')
    for b in jogador:
        sleep(0.3)
        print(f'{N}   {b["nome"]:10}    {sum(b["gols"]):>}')
        N +=1
    print(f'\033[1;31m{"=" * 80}\033[m')
sleep(0.5)
print(f'{"==>FINALIZANDO<==":^30}')

