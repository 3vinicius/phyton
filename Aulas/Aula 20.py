# Progama
def soma(*a):
    c = 0
    v = 0
    for n in a:
        c += 1
        v += n
        print(f'{n} ', end=' + ')
    print(f'= {v}')
    print(f'foram {c} números digitados')


#soma(2, 3)


# Progama que dobra valores
"""def dobravalores(*a):
    pos = 0
    while pos < len(l):
        l[pos] *= 2
        pos += 1
    print(l)"""


l = [2, 1]
l[1]*=2
print(l)