import datetime
ano = datetime.date.today().year
nascimento = int(input('Ano de nascimento :'))
idade = int(ano - nascimento)
ainda = 18 - idade
if idade < 18:
    print('Ainda vai se alistar ao serviço militar')
    print(f'Falta exatamente {ainda} anos')
elif idade == 18:
    print('É hora de se alistar ao serviço militar ')
else:
    print(f'Já passou o tempo de {idade - 18} anos para se alistar')