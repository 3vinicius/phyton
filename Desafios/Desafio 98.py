import time


def contador(i, f, p):
    print('=-'*30)
    print(f'Contagem de {i} até {f} de razão {p}')
    if i > f:
        f -= 2
    for c in range(i, f+1, p):
        time.sleep(0.5)
        print(c, end=' ')
    print('  FIM!')
    print('=-' * 30)


contador(1, 10, 1)
contador(10, 0, -2)

while True:
    inicio = int(input('Digite o inicio'))
    fim = int(input('Digite o fim'))
    passo = int(input('Digite o passo'))
    if inicio > fim and passo > 0:
        passo = -passo
    if inicio > fim and passo == 0:
        passo = -1
    elif passo == 0:
        passo = 1
    contador(inicio, fim, passo)
    p = str(input("Deseja fazer uma nova contagem [S/N]? ")).upper()
    while True:
        if p[0] in 'SN':
            break
        p = str(input("Deseja fazer uma nova contagem [S/N]? ")).upper()
    if p[0] == 'N':
        break

time.sleep(0.5)


print('-=-=-=-=-=FIM DO PROGAMA=-=-=-=-=-=-')
