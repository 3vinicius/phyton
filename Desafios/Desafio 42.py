n1 = float(input('Digite o comprimento'))
n2 = float(input('Digite o comprimento'))
n3 = float(input('Digite o comprimento'))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
if (n1 + n2 + n3 - maior) > maior:
    print('O triangulo existe')
    if n1 == n2 == n3 :
        print('É um triangulo equilatero')
    elif n1 != n2 and n2 != n3 and n1 != n3 :
        print("É um triangulo escaleno")
    else:
        print('É um triangulo isoceles')
else:
    print('O triangulo não existe')
