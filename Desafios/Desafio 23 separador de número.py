import random

n = random.randint(0,9999)

print(f'Observe o número {n}')

l = str(n)
print(f'Unidade = {l[0]}\nDesena = {l[1]}\nCentena = {l[2]}\nMilhar = {l[3]}')