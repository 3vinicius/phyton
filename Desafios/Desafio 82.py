import random
list = []
listi = []
lisp = []
for c in range(0, random.randint(0, 40)):
    list.append(random.randint(0,99))
for p in range(0, len(list)):
    if list[p]%2 == 0:
        lisp.append(list[p])
    else:
        listi.append(list[p])
print(f'Lista: {list}')
print(f'Lista Pares: {lisp}')
print(f'Lista Impar: {listi}')


