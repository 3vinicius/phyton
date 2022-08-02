from random import randint
from time import sleep
n = 'GAME ADIVINHE O NÚEMRO !!'
print(f'\033[1;31;40m{n:=^50}\033[m')
print()
v = randint(0, 10)
j = int(input('Digite um número de [0 até 10]: '))
palpites = 0
while j != v:
    palpites +=1
    print('Voçê errou !!')
    sleep(0.5)
    print()
    j = int(input('Digite um número de [0 até 10]: '))
sleep(0.7)
print()
print(f'Você acertou !!! o número é {v}')
print(f'Tentativas = {palpites} ')