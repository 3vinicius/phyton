import random
numero = int(random.randint(0, 5))
user = int(input('Digite um número de 0 - 5'))
print(f'O número é {numero}')
if numero == user:
    print('Você venceu')
else:
    print('Voçê perdeu')