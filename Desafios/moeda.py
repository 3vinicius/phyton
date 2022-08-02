# metade
def metade(n, format=False):
    n /= 2
    if format == False:
        return n
    else:
        n = valormone(n)
        return n


# dobro


def dobro(n, format=False):
    n *= 2
    if format == False:
        return n
    else:
        n = valormone(n)
        return n


# aumentado 10%


def aumentado10(n, p, format=False):
    n = (n*p/100)+n
    if format == False:
        return n
    else:
        n = valormone(n)
        return n


# reduxindo 13%


def reduz13(n, p, format=False):
    n = (-n*p/100) + n
    if format == False:
        return n
    else:
        n = valormone(n)
        return n


def valormone(n):
    n = f'{n:.2f}'
    n = str(n).replace('.',',')
    vm = n+" R$"
    return vm

def resumo(v, a, d):

    print('-'*30)
    print(f'\033[1m{"RESUMO DO VALOR":^30}\033[m')
    print('-' * 30)

    print(f'{"Preço Analizado :":<20}', end='')
    print(f'{valormone(v):<}')

    print(f'{"Dobro do presço :":<20}', end='')
    print(f'{dobro(v, format=True)}')

    pal = f'Desconto de {d}% :'
    print(f'{pal:<20}', end='')
    print(f'{reduz13(v, d, format=True):<}')

    pal = f'Aumento de {a}% :'
    print(f'{pal:<20}', end='')
    print(f'{aumentado10(v, a, format=True):<}')
    print('-' * 30)



