"""""""""""""""def contador (i, f, p):
    """"jogue o joguin""""
    c = i
    while c <= f:
        print(f'{c}', end= ' ')
        c +=p
    print('Fim')

help(contador)"""""""""""

"""
def test():
    global n
    n = 20
    print(f'Na função teste, n vale {n}')
  
# Progama principal
n = 2
print(f'No progama principal, n vale {n}')
test()
print(f'No progama principal, n vale {n}')"""

"""def soma(a=0, b=0, c=0):
    s = a+b+c
    return s



r = soma(2,3,4)
d = soma(2,1)

print(f'r = {r}  d = {d}')"""


def fator(a):
    v = 1
    for c in range (1, a+1):
        v = v*c
    return v


n = int(input("Digite um número: "))
print(f'O fatoria {n} é igual a {fator(n)}')








