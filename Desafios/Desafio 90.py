dic = {}
dic['Nome'] = input("Nome ")
dic['Medía'] = int(input("Média "))
if dic['Medía'] >= 7:
    dic['Situação'] = 'APROVADO'
else:
    dic['Situação'] = 'REPROVADO'
for k,v in dic.items():
    print(f'{k}: {v}')
