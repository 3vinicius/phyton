text = 'CADERNETA DIGITAL'
print(f'\033[1m{text:=^30}\033[m')
list = []
bibli = []
r = "z"
c = 0
while r!= 'N':
    c += 1
    nome = str(input('NOME:'))
    Nota1 = float(input("NOTA 1"))
    Nota2 = float(input("NOTA 2"))
    list.append(nome)
    list.append(Nota1)
    list.append(Nota2)
    bibli.append(list[:])
    list.clear()
    r = str(input('Quer continuar? [S/N]')).upper()
print('-='*30)
print('n°    NOME          MÉDIA')
print('-'*30)
for p in range(0, len(bibli)):
    s = bibli[p][1]+(bibli[p][2])/2
    print(f'{p}   {bibli[p][0]:<10}',f'{s:>10}')
n = 0
while n != 999:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'As notas de {bibli[n][0]} são {bibli[n][1]} {bibli[n][2]}')
print('-'*30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')



