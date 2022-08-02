n1 = float(input('Digite um número'))
n2 = float(input('Digite um outro número'))
print('MENU\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
op = int(input('Digite a opção: '))

while op != 5:
    if op == 1:
        print(n1+n2)
        print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
        op = int(input('Digite a opção: '))
    if op == 2:
        print(n1*n2)
        op = int(input('Digite a opção: '))
    if op == 3:
        if n1 > n2:
            print(f'{n1} é o mairo número')
        if n2 > n1:
            print(f'{n2} é o mairo número')
        else:
            print('Os números são iguais')
        op = int(input('Digite a opção: '))
    if op == 4:
        n1 = float(input('Digite um número'))
        n2 = float(input('Digite um outro número'))
        op = int(input('Digite a opção: '))
print('Saindo...')