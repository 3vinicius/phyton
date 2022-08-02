n = int(input("Digite q quantidade de elementos"))
q = 2
t1 = 0
t2 = 1
print(f'{t1}-', end= "")
print(f'{t2}-', end= "")
while q != n:
    q += 1
    t3 = t1 + t2
    print(f'{t3}-', end='')
    t1 = t2
    t2 = t3
print("FIM")



