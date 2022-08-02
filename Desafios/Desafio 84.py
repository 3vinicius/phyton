list = []
#dados = [['joao',32],['maria', 42],['vinicius',90],['pedro',32],['carlos', 90],['josue',34],['mateus',90]]
dados = []
listp = []
listl = []
listn = []
q = 0
p = 1
while p != '000':
    p = str(input('Digite o nome da pessoa: '))
    if p == '000':
        break
    list.append(p)
    i = int(input('Digite seu peso: '))
    list.append(i)
    q += 1
    dados.append(list[:])
    list.clear()
print('{:-^50}'.format('DADOS'))
for c in range(0, len(dados)):
    listp.append(dados[c][1])
    listl.append(dados[c][0])
listp.sort()
pesado = listp[len(listp)-1]
leve = listp[0]
print(f'{q} pessoas foram cadastradas')
for c in range(0, len(dados)):
    if c == 0:
        print(f'Os mais pesados com {pesado}Kg são', end=' ')
    if dados[c][1] >= pesado:
        print(f'[{dados[c][0]}]', end= ' ')
print()
for d in range(0, len(listp)):
    if d == 0:
        print(f'Os mais leves com {leve}Kg são', end=' ')
    if dados[d][1] <= leve:
        print(f'[{dados[d][0]}]', end= ' ')
print()
