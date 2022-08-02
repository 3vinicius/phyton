import datetime
ano = datetime.date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = ano - nasc
if idade <= 9:
    print('\033[1;34mAtleta Mirim\033[m')
elif 9 < idade <= 14:
    print('\033[1;34mAtleta Infantil\033[m')
elif 14 < idade <= 19:
    print('\033[1;34mAtleta Junior\033[m')
elif 19 < idade <= 20:
    print('\033[1;34mAtleta Sênior\033[m')
else:
    print('\033[1;34mMaster\033[m')
