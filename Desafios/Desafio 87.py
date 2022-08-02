list = [[],[],[]]
p = 0
for c in range(1, 10):
    if c <= 3:
        r = int(input(f'Digite o número [{0}, {c}]'))
        list[0].append(r)
        if r%2 ==0:
            p += r
    if 3 < c <= 6:
        r = int(input(f'Digite o número [{1}, {c}]'))
        list[1].append(r)
        if r%2 ==0:
            p += r
    if c > 6:
        r = int(input(f'Digite o número [{1}, {c}]'))
        list[2].append(r)
        if r%2 ==0:
            p += r
print('{:-^20}'.format('DADOS'))
s3 = 0
for l in range(0,3):
    s3 += list[l][2]
print(f'Soma dos valores pares: {p}')
print(f'Soma dos valores da terceira coluna: {s3}')
list[1].sort()
print(f'O maior valor da segunda linha: {list[1][2]}')
print(f'[   {list[0][0]}   ][   {list[0][1]}   ][   {list[0][2]}   ]\n'
      f'[   {list[1][0]}   ][   {list[1][1]}   ][   {list[1][2]}   ]\n'
      f'[   {list[2][0]}   ][   {list[2][1]}   ][   {list[2][2]}   ]')

