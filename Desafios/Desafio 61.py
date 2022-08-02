termo1 = int(input("Digite o primeiro termo"))
r = int(input('Digite a razão'))
valor = termo1
termos = 1
while termos != 11:
    termos += 1
    print(f'{valor}→', end='')
    valor = valor + r
print('FIM')