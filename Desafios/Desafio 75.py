n1 = int(input("Digite um número"))
n2 = int(input("Digite um número"))
n3 = int(input("Digite um número"))
n4 = int(input("Digite um número"))
list = (n1, n2, n3, n4)
valor9 = list.count(9)
p = 0
for n in range(0,3):
    if list[n] % 2 == 0:
        p +=1
if valor9 == 0:
    print('O número 9 apareceu nenum vez')
else:
    print(f'O número 9 paraceu em um total de {valor9} vezes')
if list.count(3) == 0:
    print(f'O número 3 apareceu não aparece')
else:
    posicao3 = list.index(3)
    print(f'O número 3 apareceu primeiro na posição {posicao3}')
print(f'{p} númeors são pares')