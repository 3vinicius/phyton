# Import
from random import randint

# def
def sorteia(*a):
    for l in a:
        while True:
            s = l[randint(0, len(l)-1)]
            lsort.append(s)
            if len(lsort) == 5:
                break


def somapar(a):
    lpar = []
    t = 0
    print(f'Os valores sorteados foram {a}')
    for l in a:
        if l != 0 and l % 2 == 0:
            lpar.append(l)
            t += l
    print(f'Os valores pares são {lpar} Total = {t}')

lsort =[]
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteia(l)
somapar(lsort)
