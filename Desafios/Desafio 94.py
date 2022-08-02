from time import sleep
dic = {}
list = []
#list =[{'nome': 'vinicius', 'idade': 22, 'sexo': 'M'}, {'nome': 'luana', 'idade': 24, 'sexo': 'F'}, {'nome': 'lucas', 'idade': 25, 'sexo': 'M'}, {'nome': 'mylena', 'idade': 22, 'sexo': 'F'}, {'nome': 'amorim', 'idade': 25, 'sexo': 'M'}, {'nome': 'mariana', 'idade': 35, 'sexo': 'F'}, {'nome': 'rogerio', 'idade': 40, 'sexo': 'M'}, {'nome': 'eraldo', 'idade': 43, 'sexo': 'M'}, {'nome': 'dindinha', 'idade': 79, 'sexo': 'F'}]
lm = []
r = 'S'
c = 0
while r != 'N':
    sleep(0.5)
    print(f'\033[1m{" NOVO CADASTO ":=^70}\033[m')
    print()
    c += 1
    dic['nome'] = str(input("Digite seu nome: ")).capitalize()
    idade = int(input('Digite sua idade: '))
    while True:
        if idade > 0:
            break
        if idade < 200:
            break
        idade = int(input('Digite sua idade, um valor entre 0 - 200: '))
    dic['idade'] = int(idade)
    sexo = str(input('Digite seu sexo [M/F] ')).upper()
    while True:
        if sexo == "MF":
            break
        print('Valor invalido')
        sexo = str(input('Digite seu sexo [M/F] ')).upper()
    dic['sexo'] = sexo[0]
    list.append(dic.copy())
    dic.clear()
    r = input("Deseja fazer um novo cadastro [S/N]: ").upper()
    while True:
        if r in "SN":
            break
        print('Erro !!!')
        r= input("Digite o valor correto [S/N]: ").upper()
si = 0
s = c
sleep(0.6)
print()
print(f'\033[1m{"- DADOS -":=^70}\033[m')
print()
sleep(0.4)
print(f'[A] {s} pessoas foram cadastradas')
print()
for d in list:
    si += d['idade']
sleep(0.3)
print(f'[B] A médiadas idades é {si/s:2f}')
print()
print('[C]As mulheres cadastradas foram: ', end='' )
for d in list:
    sleep(0.1)
    if d['sexo'] == 'F':
        print(f'{d["nome"]}', end=' ')
print()
print()
lm.clear()
print('[D]As pessoas que estão acimada media são:')
for d in list:
    if d['idade'] > si/s:
        print(f'=>  {d["nome"]} do sexo {d["sexo"]} idade: {d["idade"]}' )
print()
print('FINALIZANDO ! ', end='')
for d in range(3,-1,-1):
    print(f"{d}..", end= '')
    sleep(0.5)
print()
print(f'{"==>VOLTE SEMPRE<==":^40}')




