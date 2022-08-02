### pessoa 1
print('DADOS 1')
nome1 = str(input('Qual é seu nome'))
idade1 = int(input('Qual a sua idade'))
sexo1 = str(input("Qual o sexo M ou F"))
print()

### pessoa 2
print('DADOS 2')
nome2 = str(input('Qual é seu nome'))
idade2 = int(input('Qual a sua idade'))
sexo2 = str(input("Qual o sexo M ou F"))
print()
### pessoa 3
print('DADOS 3')
nome3 = str(input('Qual é seu nome'))
idade3 = int(input('Qual a sua idade'))
sexo3 = str(input("Qual o sexo M ou F"))
print()

### pessoa 4
print('DADOS 4')
nome4 = str(input('Qual é seu nome'))
idade4 = int(input('Qual a sua idade'))
sexo4 = str(input("Qual o sexo M ou F"))
print()

### BANCO DE DADOS
list1 = [nome1, idade1, sexo1]
list2 = [nome2, idade2, sexo2]
list3 = [nome3, idade3, sexo3]
list4 = [nome4, idade4, sexo4]
listidade = [idade1 , idade2, idade3, idade4]
listnome = [nome1, nome2, nome3, nome4]
listsexo = [sexo1, sexo2, sexo3, sexo4]
listat = [listnome, listsexo, listidade]

if listsexo[0] == 'M':
    idaeh1 = idade1
else:
    idaeh1 = 0
if listsexo[1] == 'M':
    idaeh2 = idade2
else:
    idaeh2 = 0
if listsexo[2] == 'M':
    idaeh3 = idade3
else:
    idaeh3 = 0
if listsexo[3] == 'M':
    idaeh4 = idade4
else:
    idaeh4 = 0
listidadeh = [idaeh1, idaeh2, idaeh3, idaeh4]

from time import sleep
###DADOS
sleep(0.2)
print('RESULTADOS !!!')
sleep(0.5)
print()
med = (idade4+idade3+idade2+idade1)/4
print(f'Media das idades: {med}')

q = 0
s = 0
for c in range(0, 4):
    if listsexo[c] == 'M' and listidadeh[c] >= listidadeh[0] and listidadeh[c] >= listidadeh[1] and listidadeh[c] >= listidadeh[2] and listidadeh[c] >= listidadeh[3]:
        print(f'{listnome[c]} é o homem mais velho')
    if listsexo[c] == 'F' and listidade[c] < 20:
        s = s + listidade[c]
        q = q + 1
print(f'{q} mulheres tem menos de 20 anos')
print('FIM....')
