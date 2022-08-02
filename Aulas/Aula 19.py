dic = {}
list = []
for c in range (1,3):
    dic['Nome']=str(input('Nome: '))
    dic['Idade']=int(input('Idade: '))
    dic['Sexo']=str(input('Sexo [M/F]'))
    list.append(dic.copy())
    dic.clear()

for d in list:
    for v in d.items():
        print(f'{v}')