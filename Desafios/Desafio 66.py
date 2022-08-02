from time import sleep
from random import randint
text = 'CONTADOR'
print(F'\033[1;31;40m{text:^40}\033[m')
print()
q=0
s=0
a = int(input("Digite um número: "))
while True:
    q += 1
    a = randint(0,999)
    if a == 999:
        break
    s = s + a
sleep(0.5)
print(f'Soma = {s}')
print(f'Quantidade = {q}')