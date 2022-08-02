import time
print(15 * "=", " NOVO CADASTRO ", 15 * "=")
r = 'Sim'
memor = 0
h = 0
m = 0
while r != 'N':
    i = int(input('Idade: '))
    s = str(input('Sexo[M/F]: ')).upper()
    if i >= 18:
        memor += 1
    if s == "M":
        h += 1
    if s == 'F' and i < 20:
        m += 1
    a = str(input('Quer realizar um cadastro ? [SIM / NÂO] ')).upper().strip()
    r = a[0]
    print(15 * "=", " NOVO CADASTRO ", 15 * "=")
time.sleep(0.5)
print(20 * "="," DADOS ",20 * "=")
print(f'Total de pessoas maiores de idade {memor}')
print(f'Total de homes {h}')
print(f'Total de mulheres menores de 20 anos: {m}')

