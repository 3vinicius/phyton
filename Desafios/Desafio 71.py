
v = int(input('Valor do saque: '))
s = 1
vnew = v
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while vnew != 0:
    if vnew % 50 == 0:
        n50 += 1
        vnew = vnew - 50
    elif vnew % 20 == 0:
        n20 += 1
        vnew = vnew - 20
    elif vnew % 10 == 0:
        n10 += 1
        vnew = vnew - 10
    elif vnew % 1 == 0:
        n1 += 1
        vnew = vnew - 1
    s = (n50*50)+(n20*20)+(n10*10)+(n1*1)
if n50 != 0:
    print(f'{n50} cedulas de 50$')
if n20 != 0:
    print(f'{n20} cedulas de 20$')
if n10 != 0:
    print(f'{n10} cedulas de 10$')
if n1 != 0:
    print(f'{n1} cedulas de 1$')
for c in range(0, 5):
    print(c)



