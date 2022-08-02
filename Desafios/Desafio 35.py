n1 = float(input('Digite o primeiro número '))
n2 = float(input('Digite o segundo número '))
n3 = float(input('Digite o terceiro número '))
if n1 > n2:
    if n1 > n3:
        N = float(n1)
else:
    print()
if n2 > n1:
    if n2 > n3:
        N = float(n2)
else:
    print()
if n3 > n2:
    if n3 > n1:
        N = float(n3)
else:
    print()
R = n1 + n2 + n3 - N
if R > N:
    print('O triangulo existe')
else:
    print('Não existe')