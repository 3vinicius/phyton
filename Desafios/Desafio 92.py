import datetime
bibli = {}
bibli['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
bibli['idade'] = (-ano + datetime.date.today().year)
ctps = int(input(('Carteira de trabalho (0 não tem) ')))
if ctps == 0:
    bibli['ctps'] = ctps
else:
    bibli['ctps'] = ctps
    contr = int(input('Ano de contratação '))
    bibli['contratação'] = contr
    bibli['salário'] = int(input('Salário '))
    bibli['aposentadoria'] = (contr - ano) + 32
for k,v in bibli.items():
    print(f'{k} tem o valor {v}')