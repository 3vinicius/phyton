
import datetime
Ano = datetime.date.today().year
p1 = int(input('Idade da pesosa 1'))
p2 = int(input('Idade da pesosa 2'))
p3 = int(input('Idade da pesosa 3'))
p4 = int(input('Idade da pesosa 4'))
p5 = int(input('Idade da pesosa 5'))
p6 = int(input('Idade da pesosa 6'))
p7 = int(input('Idade da pesosa 7'))
I1 = Ano - p1
I2 = Ano - p2
I3 = Ano - p3
I4 = Ano - p4
I5 = Ano - p5
I6 = Ano - p6
I7 = Ano - p7
list1 = [I1, I2, I3, I4, I5, I6, I7]
menor = 7
for q in range (1 , 8):
    if list1[q-1] >= 18:
        menor = menor - 1
print(f'Tem {menor} Menor de idade ')
print(f'Tem {7 - menor} Maior de idade')