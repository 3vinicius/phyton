from time import sleep
n1 = int(input('Digite um númeo'))
n2 = int(input('Digite um número'))
sleep(1)
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')
elif n1 == n2:
    print(f'{n1} é igual a {n2}')

