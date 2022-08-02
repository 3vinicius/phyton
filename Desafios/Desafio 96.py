def area(a, b):
    s = a * b
    print(f'A = {a} x {b} \nA = {s} m²')


def lin():
    print('-'*40)


lin()
print(f'{"Calculadora de Area":^40}')
lin()
print()


l = float(input('Digite o valor da largura'))
c = float(input("Digite o valor do comprimento"))
lin()
print()
area(l, c)
