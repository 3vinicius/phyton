import random
from time import sleep
print(f'\033[1:33:40m{" JOCKENPO ":=^40}\033[m')
print()
jogador = str(input('Escolha: pedra, papel, ou tesoura ? '))
lista1 = ['pedra', 'papel', 'tesoura']
print('Calma Estou Pensando . . .')
sleep(0.5)
comp = str(lista1[random.randint(0,2)])
print(f' {comp}')
sleep(0.5)
if jogador == comp:
    print('Empate')
elif jogador == 'pedra' and comp == 'tesoura' or jogador == "tesoura" and comp == 'papel' or jogador == 'papel' and comp == 'pedra':
    print('Parabéns, infelizmente voçê venceu !!')
elif comp == 'pedra' and jogador == 'tesoura' or comp == "tesoura" and jogador == 'papel' or comp == 'papel' and jogador == 'pedra':
    print(' \033[1;31mEU GANHEI DE VOÇÊ OTARIO !!!!')
else:
    print('\033[1;31mERRO!!!!!!')
