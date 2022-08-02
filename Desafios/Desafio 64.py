from random import randint
a = randint(400, 999)
soma = 0
q = 0
while a != 999:
    q += 1
    soma = soma + a
    a = randint(400, 999)
print(f'A soma dos números é {soma}')
print(f'foram {q} somados')
